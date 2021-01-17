calories_per_strip = list(map(int, input().split()))

game_clicks = list(input())

calories_wasted = [calories_per_strip[int(game_click)-1] for game_click in game_clicks]

print(sum(calories_wasted))
