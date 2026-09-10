import sys
import json

values_path = sys.argv[1]
tests_path = sys.argv[2]
report_path = sys.argv[3]

with open(values_path, "r") as f:
    values_data = json.load(f)

with open(tests_path, "r") as f:
    tests_data = json.load(f)

results = {}
for item in values_data["values"]:
    results[item["id"]] = item["value"]

def fill_values(test):
    if "value" in test:
        test["value"] = results[test["id"]]

    if "values" in test:
        for nested_test in test["values"]:
            fill_values(nested_test)

for test in tests_data["tests"]:
    fill_values(test)

with open(report_path, "w") as f:
    json.dump(tests_data, f, indent=2)