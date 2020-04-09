
def solution(A):
    seen = [False] * len(A)
    for value in A:
        if 0 < value <= len(A):
            seen[value-1] = True

    for idx in range(len(seen)):
        if seen[idx] is False:
            return idx + 1

    return len(A)+1


if __name__ == "__main__":
    A = [[1, 3, 6, 4, 1, 2],
         [1, 2, 3],
         [-1, -3]
         ]

    for a in A:
        print()
        print(a, '\nMin missing:', solution(a))
