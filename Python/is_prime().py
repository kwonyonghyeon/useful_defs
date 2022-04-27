#is_prime() 함수는 입력된 수가 소수인지 아닌지 True or False 형태로 반환합니다.

def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i < n:
      if n % i == 0:
        return False
      i+=1
    return True
