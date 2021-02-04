n = int(input())

sizes = map(int, input().split())

waiting_list = list()

for size in sizes:
    waiting_list.append(size)

    if size == n:

        to_be_added = list()

        len_ = len(waiting_list)

        for i in range(len_):
            if n in waiting_list:
                to_be_added.append(waiting_list[waiting_list.index(n)])
                n -= 1
            else:
                break

        print(*to_be_added)

    else:
        print()
