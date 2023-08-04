def main():
    n = int(input())
    a = map(int, input().split())

    l = [(e, i) for i, e in enumerate(a)]
    s = [str(e[1] + 1) for e in sorted(l, key=lambda x: x[0])]
    print(" ".join(s))


main()
