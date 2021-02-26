num_test_cases = int(input())

outputs = list()

for i in range(num_test_cases):
    m, n = map(int, input().split())

    path = list()

    for j in range(m):
        path.insert(0, list(input()))
