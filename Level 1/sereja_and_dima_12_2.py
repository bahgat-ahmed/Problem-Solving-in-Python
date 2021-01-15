num_cards = int(input())

card_nos = list(map(int, input().split()))

last_card_no_idx = len(card_nos) - 1
sereja_sum, dima_sum = 0, 0

sereja_and_dima_sums = [0, 0]

for idx in range(len(card_nos)):

    if len(card_nos) > 1:
        choice = max(card_nos[0], card_nos[-1])
    else:
        # when there is one card no. left in the list
        choice = card_nos[0]

    sereja_and_dima_sums[idx % 2] += choice
    card_nos.remove(choice)

print(*sereja_and_dima_sums)
