def rotate(a, r):
    l = a[r:] + a[:r]
    return l


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    r = d % n

    print(*rotate(a, r))
