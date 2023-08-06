n = input()
s = input()

x = 0

l = [(x := x + 1) if e == "I" else (x := x - 1) for e in s]
print(max(0, max(l)))
