
def reverse(arr, i, j):
    for idx in range((j - i + 1) // 2):
        arr[i+idx], arr[j-idx] = arr[j-idx], arr[i+idx]


def solution(A, K):
    n = len(A)
    if n == 0:
        return []
    K = K % n
    reverse(A, n - K, n - 1)
    reverse(A, 0, n - K - 1)
    reverse(A, 0, n - 1)
    return A


def solution2(A, K):
    n = A
    if not n:
        return n
    for x in range(K):
        a = n.pop()
        n.insert(0, a)
    return n


def solution3(A, K):
    N = len(A)
    if N < 1 or N == K:
        return A
    K = K % N
    while K > 0:
        tmp = A[N - 1]
        for i in range(N - 1, 0, -1):
            A[i] = A[i - 1]
        A[0] = tmp
        K -= 1
    return A


def solution4(A, K):
    for e in range(K):
        A = [A[i-1] for i in range(len(A))]
    return A


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    K = 6

    print(A, K)
    print(solution(A, K))
