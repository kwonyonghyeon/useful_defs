#https://www.techiedelight.com/ko/program-to-find-nth-fibonacci-number/ 에서 가져왔습니다. 감사합니다!
#n과 lookup을 받습니다. lookup은 {}로 해서 사용하시면 됩니다.
#nth_fibonacii()는 n번째 피보나치 수열의 요소를 구합니다.

def nth_fibonacci(n, lookup):
    if n <= 1:
        return n
    if n not in lookup:
        lookup[n] = nth_fibonacci(n - 1, lookup) + nth_fibonacci(n - 2, lookup)
    return lookup[n]
