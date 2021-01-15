# from IPython.core.debugger import set_trace
# set_trace()
num_cards = int(input())

card_nos = list(map(int, input().split()))

last_card_no_idx = len(card_nos) - 1
sereja_sum, dima_sum = 0, 0



idx = -1

while len(card_nos) > 0:
    idx += 1

    if idx % 2 == 0:

        # sereja turn
        if len(card_nos) != 1:
            sereja_choice = max(card_nos[0], card_nos[-1])
            sereja_sum += sereja_choice
            # remove the chosen item from the list
            card_nos.remove(sereja_choice)
        else:
            # when there is one card left in the list
            sereja_sum += card_nos[0]
            # remove the chosen item from the list
            card_nos.remove(card_nos[0])
    else:
        # dima turn
        if len(card_nos) != 1:
            dima_choice = max(card_nos[0], card_nos[-1])
            dima_sum += dima_choice
            # remove the chosen item from the list
            card_nos.remove(dima_choice)
        else:
            # when there is one card left in the list
            dima_sum += card_nos[0]
            # remove the chosen item from the list
            card_nos.remove(card_nos[0])

print(sereja_sum, dima_sum)
