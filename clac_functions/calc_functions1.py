# 코딩 클럽 2권 계산기의 애플리케이션의 함수 모듈
    
# 팩토리얼 함수:
def factorial(n):
    try:
        n = int(n)
    except:
        return "--> 오류!"

    #'0'과 같은지 체크(특별한 경우):
    if n == 0:
        return 1

    #매우 큰 수인지 확인해서 돌려보냄:
    if n > 40:
        return "--> 답이 화면을 가득채울 수 있습니다!"

    #음수가 발생할 경우에 대한 점검:
    if n < 0:
        return "--> 오류!"

    #팩토리얼 알고리즘 적용:
    ans = n #반복문을 시작하기 전에 답변의 초깃값 설정
    while n > 1:
        ans = ans * (n-1)
        n = n-1
    return ans

# 로마 숫자로 변환하는 함수:
def to_roman(n):
    try:
        n = int(n)
    except:
        return str("--> 오류!")

    #인수가 4999보다 큰 숫자인지 범위를 벗어난 것으로 판단합니다:
    if n > 4999:
        return "--> 범위를 넘어섭니다."

    #튜플과 사전 생성:
    romans = ((1000 , "M"), (900, "CM"), (500 , "D"), (400 , "CD"), (100 , "C"), (90 , "XC"),(50 ,"L"), (40 , "XL") , (10,"X"), (9, "IX"), (5 ,"V"), (4, "IV"), (1 ,"I") )

    #알고리즘 시작:
    result = ""
    value = 0
    while value < len(romans):
        while n >= romans[value][0]:
            result = result+romans[value][1]
            n = n-romans[value][0]
        value = value+1
    return result
# 10진수를 2진수로 변환하는 함수:
def to_binary(n):
    try:
        n = int(n)
        return bin(n)[2:]
    except:
        return "-->오류!"

# 2진수를 10진수로 변환하는 함수:
def from_binary(n):
    try:
        return int(n, 2)
    except:
        return "--> 오류!"

# 숫자에 대해 제곱급을 찾는 함수:
def square(n):
    return float(n)**2

# 숫자에 대해 제곱근 루트를 찾는 함수:
def square_root(n):
    return float(n)**0.5
