
def solution(A):
    max_sum = 0
    cur = []

    for i, n in enumerate(A):
        if n >= 0:
            cur.append(n)
            cur_sum = sum(cur)
        if (n < 0) or (i == len(A) - 1):
            if cur_sum > max_sum:
                max_sum = cur_sum
            cur = []

    return max_sum


if __name__ == "__main__":
    a = [1, 2, 5, -7, 2, 5]
    # a = [1, 2, 5, -7, -2, 12]
    print(solution(a))
