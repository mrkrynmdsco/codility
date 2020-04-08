
def solution(N):
    binstr = bin(N)[2:].strip('0')
    binlst = str(binstr).split('1')
    return len(max(binlst))


if __name__ == "__main__":
    N = [9, 529, 20, 15, 32, 1041]

    for n in N:
        max_gap = solution(n)
        print('Input:', n, '\tMax_Gap:', max_gap)
