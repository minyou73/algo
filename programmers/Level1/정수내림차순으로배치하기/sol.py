# n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 
# 예를들어 n이 118372면 873211을 리턴하면 됩니다.

# def solution(n):
#     answer = []
#     for i in str(n):
#         answer.append(i)
#     a = ''.join(sorted(answer, reverse=True))
#     return int(a) 


# print(solution(118372))

#######################################################

def solution(n):
    answer = ''.join(sorted(str(n), reverse=True))
    return int(answer)

print(solution(118372))