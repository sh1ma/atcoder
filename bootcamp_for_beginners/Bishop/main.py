def main():
    h, w = map(int, input().split())
    a = h * w
    s = int(a / 2)

    if h == 1 or w == 1:
        exit(print(1))

    if a % 2 == 0:
        exit(print(s))
    else:
        print(s + 1)


main()
