#  my_string은 소문자, 대문자, 자연수로만 구성되어있습니다.
#  my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    sum_num = 0
    
    for i in my_string:
        if not i.isdigit():        # my_string의 글자하나씩 출력해서 그것이 숫자가 아니라면
            my_string = my_string.replace(i, ' ')  #공백으로 대체해준다

    for j in my_string.split():     # 공백으로 잘라주고
        sum_num += int(j)           # mystring 값이 문자이므로 정수형태로 변환하여 더해준다
        
    return sum_num

print(solution("aAb1B2cC34oOp"))




####################################################################
# def solution(my_string):
#     num = []
#     sum_num = 0
#     for i in my_string:
#         if i.isdigit():
#             num.append(int(i))
#     for j in num:
#         sum_num += j
#     return sum_num

# 1 2 3 4 를 각각 더해준다ㅜㅜㅜ

###############################################################

# re라이브러리+정규표현식
import re

def solution(my_string):
    num = re.findall(r'\d+', my_string)
    num = list(map(int, num))
    return sum(num)

# Python re library의 findall method는 문자열 내에서 특정 패턴을 만족하는 모든 문자열을 return해줍니다.
# 34라는 하나의 수로 인식해야 하기 때문에 1번 이상 반복되는 정수를 의미하는 r'\d+'를 패턴으로 작성해 주었다.
# [0-9] : 문자열 중에서 0 ~ 9 까지의 숫자가 들어있는 문자열은 모두 해당됩니다.
# [^ ... ] 캐럿(^)은 반대를 의미합니다. (=!)/ [^0-9] : 문자열 중에서 0 ~9 를 제외한 문자열 (a-z, A-Z)가 해당됩니다.
import re
def solution(my_string):
    answer = 0
    new_str = re.split(r"[^0-9]", my_string)
    for i in new_str:
        if i.isdigit():
            answer += int(i)
    return answer


######################################################################
def solution(my_string):
    stack = []
    for i in range(len(my_string)):
        if my_string[i].isdigit():
            # 스택이 비었을 때 - 추가
            if len(stack) == 0:
                stack.append(my_string[i])
                idx = i # 인덱스 저장하고 붙어있는 숫자인지 판단할 때 사용
            
            # 스택이 차있을 때 -     
            else:
                # 현재 인덱스 번호와 추가한 숫자 인덱스 번호 차이가 1이라면(붙어있다면)
                if i - idx == 1:
                    stack[-1] = stack[-1] + my_string[i]
                    idx = i
                # 붙어있는 숫자가 아니라면 
                else:
                    stack.append(my_string[i])
                    idx = i

    stack = map(int, stack)
    return sum(stack)