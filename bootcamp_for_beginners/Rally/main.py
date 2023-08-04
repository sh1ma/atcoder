import math


def main():
    input()
    xi = list(map(int, input().split()))

    mi = min(xi)
    ma = max(xi)

    ans = 999999

    for i in range(mi, ma + 1):
        num = sum([(x - i) ** 2 for x in xi])
        ans = min(num, ans)

    print(ans)


main()
