num_teams = int(input())

children_ids = list()

children_talents = list(map(int, input().split()))

num_talent_1, num_talent_2, num_talent_3 = children_talents.count(1), children_talents.count(2), children_talents.count(3)

max_no_teams = min(num_talent_1, num_talent_2, num_talent_3)

children_ids_sorted_by_talents = sorted(range(num_teams), key = lambda i: children_talents[i])

print(max_no_teams)

if max_no_teams > 0:

    for i in range(max_no_teams):
        print(children_ids_sorted_by_talents[i]+1, children_ids_sorted_by_talents[i+num_talent_1]+1, children_ids_sorted_by_talents[i+num_talent_1+num_talent_2]+1)
