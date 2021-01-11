# reading inputs
no_of_games = int(input())
games_results = [result for result in input()]

anton_wins, danik_wins = 0, 0

for idx, result in enumerate(games_results):
    if result == 'A' and idx < no_of_games:
        anton_wins += 1
    elif result == 'D' and idx < no_of_games:
        danik_wins += 1

    # handling no. of inputs larger than the no. of games
    if idx == no_of_games:
        break

# printing final result
if anton_wins > danik_wins:
    print("Anton")
elif anton_wins < danik_wins:
    print("Danik")
else:
    print("Friendship")
