import math

n = int(input())

for i in range(n + 1):
    if int(i * 1.08) == n:
        print(i)
        exit()
print(":(")
