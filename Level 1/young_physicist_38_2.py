print("YNEOS"[any(map(sum, zip(*[map(int, input().split()) for i in ' '*int(input())])))::2])
