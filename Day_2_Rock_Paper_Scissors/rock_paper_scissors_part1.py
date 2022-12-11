# A: Rock, B: Paper, C: Scissors
# X: Rock, Y: Paper, Z: Scissors

OUTCOMES = {
    'A': {
        'X': 3,
        'Y': 6,
        'Z': 0,
    },
    'B': {
        'X': 0,
        'Y': 3,
        'Z': 6,
    },
    'C': {
        'X': 6,
        'Y': 0,
        'Z': 3,
    }
}
SCORES = {'X': 1, 'Y': 2, 'Z': 3}


file = open('input.txt')

total_score = 0
for data in file.readlines():
    p1, p2 = data.strip().split()
    total_score += OUTCOMES.get(p1).get(p2) + SCORES.get(p2)

print(total_score)

file.close()