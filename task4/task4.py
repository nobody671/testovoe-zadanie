import sys

file_path = sys.argv[1]

f = open(file_path, "r")
nums = []
for line in f:
    nums.append(int(line))

nums.sort()

n = len(nums)
median_index = n // 2
median = nums[median_index]


moves = 0
for num in nums:
    moves = moves + abs(num - median)

if moves > 20:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу.")
else:
    print(moves)