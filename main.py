from random import randint


def find(k, lst):
    if len(lst) == 0:
        return False
    elif len(lst) == 1 and lst[0] == k:
        return True
    m = len(lst) // 2
    if lst[m] == k:
        return True
    if lst[m] < k:
        return find(k, lst[m + 1:len(lst)])
    else:
        return find(k, lst[0:m])


N = 25
my_list = [randint(1, N) for i in range(N)]
print(my_list)
print(find(3, my_list))
