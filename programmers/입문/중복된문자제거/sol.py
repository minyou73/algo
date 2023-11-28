# 문자열 my_string이 매개변수로 주어집니다. 
# my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.
# my_string은 대문자, 소문자, 공백으로 구성되어 있습니다.


def solution(my_string):
    result = []
    answer = 0
    for i in my_string:
        if i not in result:      #result 리스트에 my_string값이 없다면 append
                result.append(i)

    answer = ''.join(result)
    return answer

print(solution("people"))
print(solution("We are the world"))

##################################################
    result = ''
    result += i