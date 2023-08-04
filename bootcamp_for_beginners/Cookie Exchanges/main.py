def main():
    a, b, c = map(int, input().split())

    if a == b == c == 1:
        print(0)

    elif a == b == c:
        print(-1)

    else:
        cnt = 0
        while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
            x, y, z = a, b, c
            a = y / 2 + z / 2
            b = x / 2 + z / 2
            c = x / 2 + y / 2
            cnt += 1

        print(cnt)


main()
