file = open('input.txt')
data = list(map(set, map(str.strip, file.readlines())))

def get_priority(item):
    if item.isupper():
        return ord(item) - 38
    elif item.islower():
        return ord(item) - 96
    return 0

priorities = 0
for i in range(0, len(data), 3):
    rucksack1, rucksack2, rucksack3 = data[i:i+3]
    common_item = rucksack1.intersection(rucksack2).intersection(rucksack3).pop()
    priorities += get_priority(common_item)
print(priorities)

file.close()