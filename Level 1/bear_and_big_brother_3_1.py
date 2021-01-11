# reading inputs
limak_weight, bob_weight = map(int, input().split())
no_of_years = 0

while(limak_weight <= bob_weight):
    no_of_years += 1
    limak_weight = 3*limak_weight
    bob_weight = 2*bob_weight

print(no_of_years)
