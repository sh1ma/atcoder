import math


def solve():
    ...


def main():
    n, d = map(int, input().split())
    s = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0

    for i in range(n):
        for j in range(i + 1, n):
            r = math.sqrt(sum([abs(y - x) ** 2 for x, y in zip(s[i], s[j])]))
            if r.is_integer() and not r == 0.0:
                cnt += 1

    print(cnt)


main()
