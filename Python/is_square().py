#이 함수는 n이 제곱수인지 아닌지를 판별합니다.
#출처: https://codepractice.tistory.com/64 [코딩 연습]

def is_square(n): 
  return int(n ** 0.5) ** 2 == n
