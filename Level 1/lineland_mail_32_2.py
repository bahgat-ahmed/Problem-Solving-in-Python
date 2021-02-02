num_cities = int(input())

coordinates = list(map(int, input().split()))

for i in range(num_cities):
    print(min(abs(coordinates[i] - coordinates[i - 1]), abs(coordinates[i - num_cities + 1] - coordinates[i])), max(coordinates[i] - coordinates[0], coordinates[-1] - coordinates[i]))
