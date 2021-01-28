queue_length, num_packs = list(map(int, input().split()))
num_child_not_receive = 0

for i in range(queue_length):
    queue_i = int(input().replace(' ', ''))

    if queue_i + num_packs < 0: num_child_not_receive += 1
    else: num_packs += queue_i

print(num_packs, num_child_not_receive)
