import sys

file1_path = sys.argv[1]
file2_path = sys.argv[2]

f1 = open(file1_path, "r")
content = f1.read()
numbers = content.split()

x0, y0, rx, ry = numbers
x0 = float(x0)
y0 = float(y0)
rx = float(rx)
ry = float(ry)
print(x0, y0, rx, ry)

f2 = open(file2_path, "r")

for line in f2:
    coords = line.split()
    px, py = coords
    px = float(px)
    py = float(py)

    value = ((px - x0) / rx) ** 2 + ((py - y0) / ry) ** 2
    if value == 1:
        print(0)
    elif value < 1:
        print(1)
    else: 
        print(2)