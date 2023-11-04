# 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.

def solution(num_list):
    mul = 1
    su = 0
    for i in num_list:
        mul *= i
        su += i

    if mul < su ** 2:
        return 1
    else:
        return 0
 

print(solution([3, 4, 5, 2, 1]))