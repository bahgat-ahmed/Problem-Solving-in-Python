num_teams = int(input())

children_talents = [[], [], []]

for i, children_talent in enumerate(map(int, input().split())):
    children_talents[children_talent - 1].append(i + 1)

max_no_teams = min(len(children_talents[i]) for i in range(3))

print(max_no_teams)

for i in range(max_no_teams):
    print(*[children_talents[j][i] for j in range(3)])
