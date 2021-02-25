list1 = ['f', 'f', 'a', 'c', 'f', 'c', 'a']


def f(s):
    print(s)
    return sum(map(ord, s))


print(sorted(list1, key=lambda k: f(k), reverse=False))
