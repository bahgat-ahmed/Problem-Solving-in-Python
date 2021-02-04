n = int(input())

sizes = map(int, input().split())

waiting_list = list()

for size in sizes:
    waiting_list.append(size)

    if size == n:
        waiting_list.sort(reverse=True)
        needed_index = waiting_list.index(n)
        to_be_added = list()

        for idx, size_ in enumerate(waiting_list):
            current_size = size_
            if idx == needed_index:
                previous_size = size_
                to_be_added.append(size_)
            elif (idx > needed_index) and (current_size == previous_size - 1):
                to_be_added.append(size_)
                previous_size = size_

        for i in to_be_added:
            waiting_list.remove(i)

        print(*to_be_added)
        n = min(to_be_added) - 1

    else:
        print()
