word = input()

previous_letter = 'a'

min_rotations = 0

for char in word:

    distance_1 = abs(ord(previous_letter) - ord(char))
    distance_2 = 26 - distance_1
    min_rotations += min(distance_1, distance_2)
    previous_letter = char

print(min_rotations)    
