import math

# Parse input
lines = []
with open("input.txt") as f:
    lines = f.readlines()

calories_per_elf = []
elf_calories = 0

for line in lines:
    # Handle new line
    if ord(line[0]) == 10:
        calories_per_elf.append(elf_calories)
        elf_calories = 0

    # Handle number
    else:
        line_calories = int(line)
        elf_calories += line_calories

calories_per_elf.sort(reverse=True)
print(f"The three elves with the most calories are carrying a total of {calories_per_elf[0] + calories_per_elf[1] + calories_per_elf[2]} calories")
