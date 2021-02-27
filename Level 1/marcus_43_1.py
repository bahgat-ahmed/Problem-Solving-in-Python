num_test_cases = int(input())

path_letters = 'IEHOVA#'
all_commands = list()

for i in range(num_test_cases):
    current_commands = list()
    m, n = map(int, input().split())

    path = list()

    for j in range(m):
        path.insert(0, list(input()))

    current_pos = path[0].index('@')
    idx = 0
    for letter in path_letters:
        if letter in path[idx]:
            destination_pos = path[idx].index(letter)
            if destination_pos > current_pos:
                current_commands.append('right')
            else:
                current_commands.append('left')
        else:
            idx += 1
            destination_pos = path[idx].index(letter)
            current_commands.append('forth')

        current_pos = destination_pos

    all_commands.append(current_commands)

for commands in all_commands:
    print(*commands)
