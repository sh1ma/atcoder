import re


def main():
    s = input()

    reg = re.compile(r"[ACGT]+")
    r = reg.findall(s)
    if len(r) == 0:
        print(0)
        return
    m = max([len(e) for e in r])
    print(m)


main()
