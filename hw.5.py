def read_single_digit(n):
    if n == 1:
        return'일'
    if n == 2:
        return'이'
    if n == 3:
        return'삼'
    if n == 4:
        return'사'
    if n == 5:
        return'오'
    if n == 6:
        return'육'
    if n == 7:
        return'칠'
    if n == 8:
        return'팔'
    if n == 9:
        return'구'
    if n == 0:
        return'영'


def read_number(num):
    h =read_single_digit(num // 100)  # 백의 자리 숫자
    t =read_single_digit((num % 100) // 10)  # 십의 자리 숫자
    o =read_single_digit(num % 10)  # 일의 자리 숫자
    return h+t+o
    
num = int(input('세 자리 정수를 입력하시오. '))
print(read_number(num))
