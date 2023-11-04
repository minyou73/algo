#  문자열에 있는 숫자를 차례대로 더하려고 합니다. 이 때 "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다.
#  숫자와 "Z"로 이루어진 문자열 s가 주어질 때, 머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.

# 공백 기준으로 split을 해서 더한다
# z 가 나오면 전에 숫자 뺼셈


# def solution(s):
#     s_list = list(s.split())
#     plus = 0
#     answer = 0
#     for i in s_list:
#         if i.isdigit():
#             plus += int(i)
#         else:
#             a=0
#             a = s_list[(s_list.index(i))-1]    # a = s_list[i-1]
#             plus = plus - int(a)
#     return plus


# print(solution("1 2 Z 3"))   #통과 되는데
# print(solution("10 Z 20 Z 1")) #통과 안된다


#############################################################
# def solution(s):
#     s_list = list(s.split())        # s는 문자열
#     plus = 0
#     answer = 0
#     for i in range(len(s_list)):
#         if s_list[i].isdigit():     
#             plus += int(s_list[i])
#         else:
#             a = s_list[i-1]
#             plus = plus - int(a)
#     return plus



# print(solution("-1 -2 -3 Z"))
# 통과가 안된다...ㅠ
# ㅋㅋㅋㅋ 마이너스, 소수점은 문자로 판단된다...........ㅎ

################################################################

def solution(s):
    s_list = list(s.split())        # s는 문자열
    plus = 0
    answer = 0
    for i in range(len(s_list)):
        if s_list[i] == 'Z':
            a = s_list[i-1]
            plus = plus - int(a)
        else:
            plus += int(s_list[i])
    return plus



print(solution("-1 -2 -3 Z"))
#################################################################
# 스택으로도 풀수 있을거같은데..?
def solution(s):
    s_list = s.split()
    stack = []
    for i in s_list:
        if i == 'Z':
            stack.pop()
        else:
            stack.append(int(i))
    return sum(stack)
        
print(solution("-1 -2 -3 Z"))
###################################################################
def solution(s):
    stack = []
    for num in s.split(' '):
        try:
            stack.append(int(num))
        except:
            stack.pop()
    return sum(stack)

############################################################
def solution(s):
    answer = []
    
    for num in s.split():
        if num == "Z":
            answer.pop()
            continue
        answer.append(int(num))
        
    return sum(answer)