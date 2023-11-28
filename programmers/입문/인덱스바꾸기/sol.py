#문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, 
#my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.

#문자열을 일단 리스트로 바꾼다
#swap


def solution(my_string, num1, num2):
    answer = ''
    switch = 0
    string = list(my_string)

    switch = string[num1]

    string[num1] = string[num2]
    string[num2] = switch

    answer = ''.join(string)
    return answer

print(solution("I love you", 3 , 6))

##############################################################
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s)