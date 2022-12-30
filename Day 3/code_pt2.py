with open("input.txt") as f:
    lines = f.readlines()


priorities = {}
# Add keys for lowercase letters
for i in range(1, 27):
    priorities[chr(i + 96)] = i
# Add keys for uppercase letters
for i in range(27, 53):
    priorities[chr(i + 38)] = i

priorities_total = 0


for line in range(0, len(lines[:]), 3):
    """
    1: isolate groups of three strings
    2: identify character present in all three strings
    3: quantify priority value of common character
    4: total
    """
    # isolate group of three strings
    line1 = lines[line][:-1]
    line2 = lines[line+1][:-1]
    line3 = lines[line+2][:-1]

    # identify character present in all three strings
    line2Dict = {}
    for character in line2:
        if character in line2Dict:
            continue
        else:
            line2Dict[character] = True

    line3Dict = {}
    for character in line3:
        if character in line3Dict:
            continue
        else:
            line3Dict[character] = True

    line1Dict = {}
    for character in line1:
        if character in line1Dict:
            continue
        else:
            line1Dict[character] = True
        
        if character in line2Dict:
            if character in line3Dict:
                # 3: quantify priority value of common character
                char_priority = priorities[character]
                # 4: total
                priorities_total += char_priority

print(priorities_total)