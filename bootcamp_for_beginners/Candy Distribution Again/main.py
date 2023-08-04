def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    if x > sum(a) and x % sum(a) > 0:
        print(len(a) - 1)
    else:
        a = sorted(a)
        cnt = 0
        for i in a:
            if x >= i:
                x -= i
                cnt += 1
            else:
                break
        print(cnt)


main()
