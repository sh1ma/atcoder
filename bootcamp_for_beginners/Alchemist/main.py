import functools


def main():
    n = int(input())
    v = map(int, input().split())
    l = sorted(v)

    r = functools.reduce(lambda x, y: (x + y) / 2, l)
    print(r)


main()
