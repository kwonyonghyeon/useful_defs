#gcd_EuclideanAlgorithm() 함수는 유클리드 호제법을 이용하여 최대공약수(Greatest Common Divisor, GCD)를 구하는 함수입니다.

def gcd(a, b):
    while b > 0:
        a, b = min(a, b), max(a, b)
        a, b = a, int(b%a)
    return a
