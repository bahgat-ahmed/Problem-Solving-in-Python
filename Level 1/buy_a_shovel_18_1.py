input_nums = list(map(int, input().split()))

shovel_price, coin_denomination = input_nums[0], input_nums[1]

num_shovels_buy = 1
total_shovel_price = shovel_price

while ((total_shovel_price % 10) != coin_denomination) and ((total_shovel_price % 10) != 0):

    num_shovels_buy += 1
    total_shovel_price += shovel_price

print(num_shovels_buy)
