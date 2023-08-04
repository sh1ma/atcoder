import math


def main():
    n = int(input())
    k = int(input())
    xs = map(int, input().split())

    print(sum([min(x, k - x) * 2 for x in xs]))


main()
