# i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다.
#  예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다. 
#  정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요
#  n/1 ,n/2 , n/3, n/4 ...


# def solution(n):
#     answer = 0
#     for i in range(1,10 ):
#         n /= i
#     return n

# print(solution(3628800))
# 이렇게 하면 7일때 index outof range가 나온다.

##################################################################

def solution(n):
    i = 1   # 0부터 나누면 안되니까 1부터 시작
    while n//i > 0:
        n //= i   # //: 몫
        i += 1    # i 1씩 증가 해서 나누기 1, 나누기 2, 나누기 3...
    return i-1

print(solution(3628800))
print(solution(7))
#######################################################################

from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k

#############################################################
import math

def solution(n):
    i = 1
    while math.factorial(i) <= n:
        i +=1
    return i-1

    # while문을 돌려서 result ! 값이 n값보다 클때 멈춘다.