num_participants, kth_place = map(int, input().split())

scores = [*map(int, input().split())]

print(len([1 for score in scores if (score > 0) and (score >= scores[kth_place - 1])]))
