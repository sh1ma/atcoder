n, a, b = map(int, input().split())

ab = a + b

x, y = n // ab, n % ab
z = x * a
if y >= a:
    print(z + a)
else:
    print(z + y)
