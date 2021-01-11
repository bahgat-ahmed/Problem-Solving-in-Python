no_of_problems = int(input())
no_pbs_to_finally_solve = 0

for i in range(no_of_problems):
    friends_no_pb_or_not = map(int, input().split())
    if sum(friends_no_pb_or_not) >= 2:
        no_pbs_to_finally_solve += 1

print(no_pbs_to_finally_solve)        
