def TotalCount(M, N, P, Q):
    count = 0
    for l in range(M, N + 1):
        for b in range(P, Q + 1):
            count += CountPerChocolateBar(l, b)
    return count


def CountPerChocolateBar(l, b):

    count = 0
    while True:
        longerr = max(l, b)
        shorterr = min(l, b)
        count += 1
        diff = longerr - shorterr
        if diff == 0:
            return count
        else:
            l = min(l, b)
            b = diff


if __name__ == "__main__":
    M = int(input())
    N = int(input())
    P = int(input())
    Q = int(input())
    tc = TotalCount(M, N, P, Q)
    print(tc)