num_friends = int(input())

friend_gave_present_to = list(map(int, input().split()))

print(' '.join([str(friend_gave_present_to.index(i) + 1) for i in range(1, num_friends + 1)]))
