def shellSort(A): # Al0...n-1] : 정렬할 리스트
    H = gapSequence(len(A))
    for h in H: # H = [he, h1, ..., 11: 24 49
        for k in range (h):
            stepInsertionSort(A, k, h)

def stepInsertionSort(A, k:int, h:int): # Alk, k+h, k+2h, ...18 Smact
    for i in range(k + h, len(A), h):
        j = 1 - h
        newItem = A[i]
        # 이 지점에서 ALe a , 1-2h, 1-h, 31는 이미 정렬되어 있는 상태임 
        # # AL..., 1-2h, j-h, 3, j4h]의 맞는 곳에 ALS+N]를 산입한다
        while 0 < j and newItem < A[j]:
            A[j + h] = A[j]
            j -= h
        A[j+ h] = newItem

def gapSequence(n:int) -> list: # 캡 수열 만들기. 다양한 선택이 있음
    H = [1]; gap = 1
    while gap < n/5:
        gap = 3 * gap + 1
        H. append(gap)
    H.reverse()
    return H


def main():
    print("shellSort test")
    A = [3, 8, 2, 24, 8, 1, 12,1, 0, 55, 23, 44, 3, 57, 256, 11, 9, 3, 4, 5, 6, 36, 912, 23, 4, 2, 55, 0, 256, 333, 23, 65]
    print("A[]:       ", A)
    shellSort(A)
    print("Sorted A[]:", A)

if __name__ == "__main__":
    main()

