import math


def main():
    a = int("".join(input().split()))
    rooted = math.sqrt(a)
    if rooted.is_integer():
        print("Yes")
    else:
        print("No")


main()
