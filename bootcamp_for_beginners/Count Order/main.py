from itertools import permutations


def main():
    n = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))

    l = list(permutations(range(1, n + 1)))

    a = [i for i, t in enumerate(l) if t == p or t == q]
    if len(a) == 1:
        print(0)
        return
    print(abs(a[0] - a[1]))


main()
