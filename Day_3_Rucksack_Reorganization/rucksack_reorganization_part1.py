file = open('input.txt')

def get_priority(item):
    if item.isupper():
        return ord(item) - 38
    elif item.islower():
        return ord(item) - 96
    return 0

priorities = 0
for line in file.readlines():
    data = line.strip()
    compartment1 = set(data[:len(data)//2])
    compartment2 = set(data[len(data)//2:])
    common_item = compartment1.intersection(compartment2).pop()
    priorities += get_priority(common_item)
print(priorities)

file.close()