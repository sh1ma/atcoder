def main():
    n = int(input())
    d = map(int, input().split())

    s = sorted(d)
    div = int(len(s) / 2)
    a, b = s[:div], s[div:]

    print(b[0] - a[-1])


main()
