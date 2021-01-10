
no_of_friends, fence_height = map(int, input().split())

# friend_heights = list(map(int, input().split()))
# limiting number of friend_heights in the list to those the user specified
friend_heights = [int(friend_height) for idx, friend_height in enumerate(input().split()) if idx < no_of_friends]

min_width = 0

for friend_height in friend_heights:
    if friend_height <= fence_height:
        min_width = min_width + 1
    else:
        min_width = min_width + 2

print(min_width)
