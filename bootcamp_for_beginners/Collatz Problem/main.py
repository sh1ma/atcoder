def main():
    s = int(input())
    l = []
    l.append(s)  # 初項
    while not (s := f(s)) in l:
        l.append(s)

    print(len(l) + 1)  # 最後の項を追加


def f(n):
    if n % 2 == 0:
        return n / 2
    return 3 * n + 1


main()
