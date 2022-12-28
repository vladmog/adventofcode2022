lines = []
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


for line in lines[:]:
    """
    1: split line in half
    2: identify character present in both halfs
    3: quantify priority of character
    4: add to total
    """
    
    # split line in half
    half1  = line[:len(line)//2]
    half2 = line[len(line)//2:-1]

    # identify character present in both halfs
    dup = 0
    is_dup_found = False
    char_index = 0

    while is_dup_found == False:
        character = half1[char_index]
        if character in half2:
            dup = character
            is_dup_found = True
        char_index += 1

    # quantify priority of character
    char_priority = priorities[dup]
    
    # add to total
    priorities_total += char_priority

print(priorities_total)