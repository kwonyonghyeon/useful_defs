#is_prime() 함수는 입력된 수가 소수인지 아닌지 True or False 형태로 반환합니다.

import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
