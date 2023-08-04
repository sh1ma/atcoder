def main():
    n, k = map(int, input().split())

    print(min(min(abs(n % k - k), n % k), n))


main()
