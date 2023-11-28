# left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고,
# 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.


def solution(left, right):

    numbers = [i for i in range(left, right+1)]
    
    answer_li = []
    
    for num in numbers:
        li = []
        for j in range(1,num+1):
            if num % j == 0:
                li.append(j)
        answer_li.append(len(li))
   
    for k in answer_li:
        if k % 2 == 0:


#     # 짝수 양수 덧셈/ 홀수 음수 덧셈


print(solution(24,27))