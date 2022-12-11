from bisect import insort

file = open('input.txt')

calories = list()
current_calories = 0
for line in file.readlines():
    data = line.strip()
    if data:
        current_calories += int(data)
    else:
        insort(calories, current_calories)
        current_calories = 0

print(calories[-1])
print(sum(calories[-3:]))

file.close()
