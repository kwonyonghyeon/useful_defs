#binary_search() 함수는 array와 x를 입력받아, array 안에 x가 있으면 True, 없으면 False를 반환합니다.

def binary_search(array, x):
    start = 0
    end = len(array) - 1 
    while start <= end:
        middle = (start + end) // 2
        if array[middle] == x:
            return True
        elif array[middle] < x:
            start = middle + 1
        else:
            end = middle - 1
    return False
