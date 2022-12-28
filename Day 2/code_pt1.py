lines = []
with open("input.txt") as f:
    lines = f.readlines()

print(lines)

moves = {
    "A": ["rock", 1],
    "B": ["paper", 2],
    "C": ["scissors", 3],
    "X": ["rock", 1],
    "Y": ["paper", 2],
    "Z": ["scissors", 3]
}


outcomes = {
    "rock": {
        "rock": 3,
        "paper": 0,
        "scissors": 6
    },
    "paper": {
        "rock": 6,
        "paper": 3,
        "scissors": 0
    },
    "scissors": {
        "rock": 0,
        "paper": 6,
        "scissors": 3
    }
}


"""
rock: 1
paper: 2
scissors: 3

win: 6
draw: 3
loss: 0
"""

total_pts = 0

for line in lines:
    opponent = line[0]
    opponent_choice = moves[opponent][0]


    you = line[2]
    you_choice = moves[you][0]
    you_choice_pts = moves[you][1]

    outcome_pts = outcomes[you_choice][opponent_choice]
    
    pts = you_choice_pts + outcome_pts
    total_pts += pts

print(total_pts)


    