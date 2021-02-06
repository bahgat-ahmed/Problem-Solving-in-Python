input_ = lambda: map(int, input().split())

num_participants, kth_place = input_()
scores = list(input_())

print(sum(score >= max(1, scores[kth_place - 1]) for score in scores))
