num_magnets = int(input())

num_groups = 1

for i in range(num_magnets):

    magnet_pole = input()

    if i == 0:
        previous_pole = magnet_pole
    else:
        if magnet_pole != previous_pole:
            num_groups += 1
        previous_pole = magnet_pole

print(num_groups)
