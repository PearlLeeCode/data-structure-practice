def solution(arr, idx):
    # idx보다 이후에 나오는 1의 값을 가지는 인덱스를 반환하는 코드 
    for i in range(idx,len(arr),1):
        if arr[i] == 1:
            return i
    return -1