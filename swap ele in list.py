def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    print(lst)

lst1 = [1, 2, 3, 4, 5, 6]
i, j = 3, 5
swap(lst1, i, j)
