def main():
    A, B, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    xys = [tuple(map(int, input().split())) for _ in range(M)]

    abmin = min(a) + min(b)

    r = [a[xy[0] - 1] + b[xy[1] - 1] - xy[2] for xy in xys]
    r.append(abmin)
    print(min(r))


main()
