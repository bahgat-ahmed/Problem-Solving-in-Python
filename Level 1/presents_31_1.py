num_friends = int(input())

friend_gave_present_to = map(int, input().split())

friend_received_present_from = [0] * num_friends

for idx, i in enumerate(friend_gave_present_to):
    friend_received_present_from[i-1] = idx + 1

print(*friend_received_present_from)
