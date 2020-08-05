def nonDivisibleSubset(k, s):
    modulo_classes = [0 for _ in range(k)]
    for x in s: modulo_classes[x % k] += 1

    l = min(1, modulo_classes[0])
    if k % 2 == 0:
        l += min(1, modulo_classes[k // 2])

    i = 1
    while i < (k - i):
        l += max(modulo_classes[i], modulo_classes[k - i])
        i += 1

    return l