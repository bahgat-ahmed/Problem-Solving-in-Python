num_cities = int(input())

coordinates = list(map(int, input().split()))

min_coordinate = min(coordinates)

if min_coordinate < 0:
    coordinates = [coord + min_coordinate for coord in coordinates]

for idx, coord in enumerate(coordinates):
    if idx == 0:
        print(abs(coord - coordinates[idx+1]), abs(coord - coordinates[-1]))
    elif idx == num_cities - 1:
        print(coord - coordinates[idx-1], coord - coordinates[0])
    else:
        min_ = min(abs(coord - coordinates[idx+1]), coord - coordinates[idx-1])
        max_ = max(abs(coord - coordinates[-1]), coord - coordinates[0])
        print(min_, max_)
