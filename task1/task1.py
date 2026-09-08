import sys


def get_path(n, m):

    path = []
    pos = 1

    while True:
        value = ((pos - 1) % n) + 1
        path.append(value)
        end = ((pos - 1 + m - 1) % n) + 1

        if end == 1:
            break

        pos = end

    return path

n1 = int(sys.argv[1])
m1 = int(sys.argv[2])
n2 = int(sys.argv[3])
m2 = int(sys.argv[4])

path1 = get_path(n1, m1)
path2 = get_path(n2, m2)

full_path = path1 + path2

result = ""

for number in full_path:
    result = result + str(number)

print(result)