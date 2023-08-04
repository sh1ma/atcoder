import math


def main():
    a, b = map(int, input().split())

    y = 0
    plugs = 0
    while plugs < b - 1:
        plugs += a - 1
        y += 1

    print(y)


main()
