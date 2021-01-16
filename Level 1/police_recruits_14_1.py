num_events = int(input())

# converting input into list for looping on it
events = list(map(int, input().split()))

num_hired, num_crimes, num_untreated_crimes = 0, 0, 0

for i in range(num_events):

    if events[i] > 0:
        # police officer hired
        num_hired += events[i]
    else:
        # crime happened
        if num_hired > 0:
            num_hired -= 1
        else:
            num_untreated_crimes += 1

print(num_untreated_crimes)            
