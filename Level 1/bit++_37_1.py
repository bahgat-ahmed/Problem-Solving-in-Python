num = int(input())

x = 0

for i in range(num):
    if input().find('+') != -1:
        x += 1
    else:
        x -= 1

print(x)
