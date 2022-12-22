import math

# Parse input
lines = []

with open("input.txt") as f:
    lines = f.readlines()

greatest_calories = float(-math.inf)
elf_calories = 0
total_calories = 0

new_lines = 0
num_lines = 0

for line in lines:
    # Handle new line
    if ord(line[0]) == 10:
        new_lines += 1
        if elf_calories > greatest_calories:
            greatest_calories = elf_calories
            elf_calories = 0

    # Handle number
    else:
        num_lines += 1
        line_calories = int(line)
        print(line_calories)
        elf_calories += line_calories
        total_calories += line_calories

if elf_calories > greatest_calories:
    greatest_calories = elf_calories

print(total_calories / num_lines)