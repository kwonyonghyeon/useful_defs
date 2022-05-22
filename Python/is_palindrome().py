#is_palindrome() 함수는 문자열이 팰린드롬인지 아닌지 판별하여 True 혹은 False의 형태로 반환합니다.

def is_palindrome(a):
    return a == a[::-1]
