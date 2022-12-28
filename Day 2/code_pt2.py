lines = []
with open("input.txt") as f:
    lines = f.readlines()

outcomes = {
    "A": {
        "X": 0 + 3,
        "Y": 3 + 1,
        "Z": 6 + 2
    },
    "B": {
        "X": 0 + 1,
        "Y": 3 + 2,
        "Z": 6 + 3
    },
    "C": {
        "X": 0 + 2,
        "Y": 3 + 3,
        "Z": 6 + 1
    }
}


"""
rock: 1
paper: 2
scissors: 3

win: 6
draw: 3
loss: 0

x: lose
y: draw
z: win

"""

total_pts = 0

for line in lines:
    opponent = line[0]
    you = line[2]

    outcome_pts = outcomes[opponent][you]
    total_pts += outcome_pts

print(total_pts)


    