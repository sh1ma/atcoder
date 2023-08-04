def main():
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    a3 = list(map(int, input().split()))
    n = int(input())
    bs = [int(input()) for _ in range(n)]

    bingo = [a1, a2, a3]
    punched = [
        [False, False, False],
        [False, False, False],
        [False, False, False],
    ]

    for b in bs:
        found = find_number(bingo, b)
        if found is None:
            continue
        punched[found[0]][found[1]] = True

        if checkBingo(punched):
            exit(print("Yes"))

    print("No")


def checkBingo(punched):
    for y in range(3):
        if all(punched[y]):
            return True
        elif all([punched[j][y] for j in range(3)]):
            return True
        elif all([punched[0][0], punched[1][1], [punched[2][2]]]) or all(
            [punched[0][2], punched[1][1], [punched[2][0]]]
        ):
            return True
    return False


def find_number(bingo, n):
    for y in range(3):
        try:
            index = bingo[y].index(n)
            return (y, index)
        except:
            pass
    return None


main()
