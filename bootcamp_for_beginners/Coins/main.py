# coding: utf-8


a = int(input())  # 500
b = int(input())  # 100
c = int(input())  # 50
x = int(input())

count = 0
for ce in range(c + 1):
    for be in range(b + 1):
        for ae in range(a + 1):
            if x == (50 * ce + 100 * be + 500 * ae):
                count += 1

print(count)
