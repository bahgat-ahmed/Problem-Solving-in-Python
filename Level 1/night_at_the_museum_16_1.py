word = input()

def modify_min_char_distance_dict_values_fn(alphabetics, min_char_distance_dict):
    alphabetics_len = len(alphabetics)
    # firstly centering around a
    for idx, char in enumerate(alphabetics):
        if idx <= alphabetics_len/2:
            # moving to one side of the embosser
            min_char_distance_dict[char] = alphabetics.find(char)
        else:
            # moving to the other side of the embosser
            min_char_distance_dict[char] = alphabetics_len - alphabetics.find(char)

    return min_char_distance_dict

def modify_alphabetics_order_fn(current_char, min_char_distance_dict, alphabetics):
    # splitting on the current character
    alphabetics = alphabetics.split(current_char)
    # centering alphabetics around the current character
    alphabetics = current_char + alphabetics[1] + alphabetics[0]

    return alphabetics

alphabetics = 'abcdefghijklmnopqrstuvwxyz'

# a dictionary for storing min distance to the current character
min_char_distance_dict = {}
# calculating the min_char_distance_dict by initially centering around 'a' character
min_char_distance_dict = modify_min_char_distance_dict_values_fn(alphabetics, min_char_distance_dict)

min_rotations = 0

for char in word:

    min_rotations += min_char_distance_dict[char]
    # updaing the alphabetics string by centering it around the new character
    alphabetics = modify_alphabetics_order_fn(char, min_char_distance_dict, alphabetics)
    # updating min_char_distance_dict distances from the new current character
    min_char_distance_dict = modify_min_char_distance_dict_values_fn(alphabetics, min_char_distance_dict)

print(min_rotations)
