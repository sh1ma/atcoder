def main():
    n = int(input())
    d, x = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    b = [int((d - 1) / i) + 1 for i in a]
    print(sum(b) + x)


main()
