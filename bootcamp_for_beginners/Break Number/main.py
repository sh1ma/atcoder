def main():
    n = int(input())
    counts = [count_divable(i) for i in range(1, n + 1)]
    max_count = counts.index(max(counts))
    print(max_count + 1)


def count_divable(n):
    cur = n
    cnt = 0

    while cur % 2 == 0:
        cur = int(cur / 2)
        cnt += 1

    return cnt


main()
