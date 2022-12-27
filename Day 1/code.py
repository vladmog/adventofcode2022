import math

# Parse input
lines = []

with open("input.txt") as f:
    lines = f.readlines()

greatest_calories = float(-math.inf)
elf_calories = 0

for line in lines:
    # Handle new line
    if ord(line[0]) == 10:
        if elf_calories > greatest_calories:
            greatest_calories = elf_calories
        elf_calories = 0

    # Handle number
    else:
        line_calories = int(line)
        elf_calories += line_calories

if elf_calories > greatest_calories:
    greatest_calories = elf_calories

print(f"The elf with the greatest calories had {greatest_calories} calories")