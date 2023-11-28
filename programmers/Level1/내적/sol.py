# a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.
# 이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. 
# (n은 a, b의 길이)


def solution(a,b):
    answer = 0

    for i in range(len(a)):
        answer += (a[i] * b[i])

    return answer


print(solution([1,2,3,4],[-3,-1,0,2]))

####################################################

def solution(a, b):

    return sum([x*y for x, y in zip(a,b)])