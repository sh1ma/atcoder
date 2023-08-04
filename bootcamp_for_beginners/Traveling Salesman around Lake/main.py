def main():
    k, n = map(int, input().split())
    a = [i for i in map(int, input().split())]

    x = [abs(a[i] - a[i - 1]) if i != 0 else k + a[0] - a[-1] for i in range(n)]
    x.remove(max(x))
    print(sum(x))


main()
