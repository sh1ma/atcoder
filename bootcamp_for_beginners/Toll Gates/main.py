import re


def main():
    n, m, x = map(int, input().split())
    a = list(map(int, input().split()))

    blocks = [i for i in range(1, n + 1)]

    l1 = blocks[:x]
    l2 = blocks[x:]

    print(min(len([i for i in l1 if i in a]), len([i for i in l2 if i in a])))


main()
