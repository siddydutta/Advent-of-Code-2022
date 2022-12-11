# A: Rock, B: Paper, C: Scissors
# X: Loss, Y: Draw,  Z: Win

OUTCOMES = {
    'A': {
        'X': 3,
        'Y': 1,
        'Z': 2,
    },
    'B': {
        'X': 1,
        'Y': 2,
        'Z': 3,
    },
    'C': {
        'X': 2,
        'Y': 3,
        'Z': 1,
    }
}
SCORES = {'X': 0, 'Y': 3, 'Z': 6}


file = open('input.txt')

total_score = 0
for data in file.readlines():
    p1, p2 = data.strip().split()
    total_score += OUTCOMES.get(p1).get(p2) + SCORES.get(p2)

print(total_score)

file.close()