def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0

    for x in a:
        r = sum([e * b[i] for i, e in enumerate(x)]) + c
        if r > 0:
            cnt += 1

    print(cnt)


main()
