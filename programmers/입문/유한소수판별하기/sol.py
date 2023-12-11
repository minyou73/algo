# 소수점 아래 숫자가 계속되지 않고 유한개인 소수를 유한소수라고 합니다. 
# 분수를 소수로 고칠 때 유한소수로 나타낼 수 있는 분수인지 판별하려고 합니다. 
# 유한소수가 되기 위한 분수의 조건은 다음과 같습니다.

# 기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다.
# 두 정수 a와 b가 매개변수로 주어질 때, a/b가 유한소수이면 1을, 무한소수라면 2를 return하도록 solution 함수를 완성해주세요.


# def solution(a,b):
#     a_li=[]
#     b_li=[]
#     for i in range(1,a+1):
#         if a % i == 0:
#             a_li.append(i)

#     for i in range(1,b+1):
#         if b % i == 0:
#             b_li.append(i)
    
#     div = []
#     for k in a_li:
#         for j in b_li:
#             if k == j:
#                 div.append(k)
    

#     a = a / max(div)
#     b = b / max(div)
   
#     if 2 in b_li or 5 in b_li:  ## 소인수 분해를 해야하나봐ㅜ
#         return 1
#     else:
#         return 2

# print(solution(7,20))
# print(solution(11,22))

####################################################################
def solution(a,b):
    a_li=[]
    b_li=[]
    for i in range(1,a+1):   # a의 약수
        if a % i == 0:
            a_li.append(i)

    for i in range(1,b+1):   # b의 약수
        if b % i == 0:
            b_li.append(i)
    
    div = []                # 최대공약수
    for k in a_li:
        for j in b_li:
            if k == j:
                div.append(k)
    

    a //=  max(div)        #최대공약수로 나눠줌 분모
    b //=  max(div)        #최대공약수로 나눠줌 분자
   
    answer = []  # 분모 소인수분해
    while b > 1:
        if b % 2 == 0:  # 짝수면
            answer.append(2)
            b //= 2
        else:
            for z in range(3, b+1, 2):  # 홀수면
                if b % z == 0:
                    answer.append(z)
                    b //= z
                    break

    if all(i in [2,5] for i in answer): #answer 리스트의 각 원소 i에 대해 i in [2, 5]를 검사
        return 1                        #all() 함수는 이 리스트의 모든 값이 참(True)인지 확인
    return 2

# print(solution(1, 12))
print(solution(7,20))
# print(solution(11,22))

#############################################################3

from math import gcd

