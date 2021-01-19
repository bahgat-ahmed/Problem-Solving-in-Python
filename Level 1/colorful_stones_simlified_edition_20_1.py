stones_positions = input()
instructions = input()

current_pos = 1

for instruction in instructions:
    if stones_positions[current_pos-1] == instruction:
        current_pos += 1

print(current_pos)
