num_magnets = int(input())

previous_pole, num_groups = "11", 0

for i in range(num_magnets):

    current_pole = input()
    num_groups += (previous_pole != current_pole)
    previous_pole = current_pole

print(num_groups)
