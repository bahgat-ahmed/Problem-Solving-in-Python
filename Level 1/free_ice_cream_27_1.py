queue_length, num_packs = list(map(int, input().split()))
num_child_not_receive = 0

for i in range(queue_length):
    queue_i = input()

    if queue_i[0] == '+':
        num_packs += int(queue_i.split()[-1])
    else:
        wanted_packs = int(queue_i.split()[-1])
        if num_packs >= wanted_packs:
            num_packs -= wanted_packs
        else:
            num_child_not_receive += 1

print(num_packs, num_child_not_receive)
