no_of_friends, fence_height = map(int, input().split())

# limiting number of friend_heights in the list to those the user specified
friend_heights = [int(friend_height) for idx, friend_height in enumerate(input().split()) if idx < no_of_friends]

min_width = sum([(friend_height > fence_height) + 1 for friend_height in friend_heights])

print(min_width)
