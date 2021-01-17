calories_per_strip = list(map(int, input().split()))

calories_per_strip_dict = {i+1: calories_per_strip[i] for i in range(len(calories_per_strip))}

game_clicks = list(input())

calories_wasted = [calories_per_strip_dict[int(game_click)] for game_click in game_clicks]

print(sum(calories_wasted))
