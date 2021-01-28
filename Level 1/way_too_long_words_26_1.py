n = int(input())

abbreviations = list()

for i in range(n):
    word = input()

    if len(word) > 10:
        abbreviations.append(word[0] + str(len(word)-2) + word[-1])
    else:
        abbreviations.append(word)

for abbrev in abbreviations:
    print(abbrev)    
