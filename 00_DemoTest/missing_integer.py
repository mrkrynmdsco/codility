
def solution(A):
    # TODO: still needs improvement, 66% score
    val = 1
    pos = []

    for n in A:
        if n > 0:
            pos.append(n)

    if pos:
        pos.sort()
        for i in range(1, len(pos)):
            if pos[i] != pos[i-1]:
                diff = pos[i] - pos[i-1]
                if diff > 1:
                    val = pos[i-1] + 1
                    if val not in A:
                        break
                else:
                    val = 1
                    if val not in A:
                        break
                    else:
                        val = pos[i] + 1
                        continue
            else:
                continue

    return val


if __name__ == "__main__":
    A = [[1, 3, 6, 4, 1, 2],
         [1, 2, 3],
         [-1, -3]
         ]

    for a in A:
        print()
        print(a, '\nMin missing:', solution(a))
