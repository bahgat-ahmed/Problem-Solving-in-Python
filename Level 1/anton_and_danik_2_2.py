# reading inputs
no_of_games = int(input())
games_results = input()

anton_wins, danik_wins = games_results.count('A'), games_results.count('D')

if anton_wins > danik_wins:
    print("Anton")
elif anton_wins < danik_wins:
    print("Danik")
else:
    print("Friendship")
