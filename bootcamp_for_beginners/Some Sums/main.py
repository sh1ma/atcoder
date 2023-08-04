# coding: utf-8


n, a, b = map(int, input().split())

l = [i for i in range(1, n + 1) if (x := sum(map(int, list(str(i))))) >= a and x <= b]


print(sum(l))
