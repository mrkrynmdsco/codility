
def solution(n):
    d = [0] * 30
    l = 0
    result = -1

    while n > 0:
        d[l] = n % 2
        n //= 2
        l += 1

    for p in range(1, l):
        ok = True
        for i in range(l - p):
            if d[i] != d[i + p]:
                ok = False
                break

        if ok and (p <= l // 2):
            result = p

    return result


if __name__ == "__main__":
    # n = 1651
    n = 9
    print(solution(n))
