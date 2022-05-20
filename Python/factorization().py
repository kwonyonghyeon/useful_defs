#factorization() 함수는 x의 소인수를 리스트 형태로 반환합니다.

def factorization(x): 
    d = 2 
    factorization = []
    while d <= x: 
        if x % d == 0: 
            factorization.append(d)
            x = x / d 
        else: 
            d = d + 1
    return factorization
