n, k, q = map(int, input().split())
l = [int(input()) for _ in range(q)]
points = [k for _ in range(1, n + 1)]

for i in l:
    points[i - 1] += 1


print("\n".join(["Yes" if i > q else "No" for i in points]))
