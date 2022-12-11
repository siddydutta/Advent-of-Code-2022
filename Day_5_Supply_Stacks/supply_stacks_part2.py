file = open('input.txt', 'r')
data = file.readlines()

break_index = data.index('\n')
n_stacks = int(data[break_index-1].strip().split()[-1])

stacks = [[] for _ in range(n_stacks)]
for line in map(str.strip, data[:break_index-1]):
    stack_index = 0
    for crate_index in range(1, len(line), 4):
        crate = line[crate_index]
        if crate != ' ':
            stacks[stack_index].insert(0, line[crate_index])
        stack_index += 1


for line in data[break_index+1:]:
    command = line.strip().split()
    count, frm, to = int(command[1]), int(command[3])-1, int(command[5])-1
    # Extend the destination stack from the source stack, in order
    stacks[to].extend(stacks[frm][-count:])
    stacks[frm] = stacks[frm][:-count]


for stack in stacks:
    print(stack[-1], end='')
print()

file.close()