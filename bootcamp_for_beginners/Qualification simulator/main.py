def main():
    n, a, b = map(int, input().split())
    ranks = input()

    cap = 0
    cur_b = 0

    for r in ranks:
        if cap >= a + b:
            print("No")
        elif r == "c":
            print("No")
        elif r == "b":
            if cur_b < b:
                print("Yes")
                cap += 1
                cur_b += 1
            else:
                print("No")
        elif r == "a":
            print("Yes")
            cap += 1


main()
