file = open('input.txt', 'r')

envelop_count, overlap_count = 0, 0
data = list(map(str.strip, file.readlines()))

for line in data:
    section1, section2 = line.split(',')
    start1, end1 = map(int, section1.split('-'))
    start2, end2 = map(int, section2.split('-'))

    # Check if first section is in second section
    if start1 >= start2 and end1 <= end2:
        envelop_count += 1
    # Check if second section is in first section
    elif start2 >= start1 and end2 <= end1:
        envelop_count += 1

    # Check if first section overlaps second section
    if start1 >= start2 and start1 <= end2:
        overlap_count += 1
    # Check if second section overlaps first section
    elif start2 >= start1 and start2 <= end1:
        overlap_count += 1

print(envelop_count)  # Part 1
print(overlap_count)  # Part 2

file.close()