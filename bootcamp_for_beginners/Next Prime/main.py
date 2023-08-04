def main():
    s = int(input())
    while not is_prime(s):
        s += 1
    print(s)


def is_prime(n):
    a = len([i for i in range(2, n) if n % i == 0]) == 0
    return a


main()
