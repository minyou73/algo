# 소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다.
#  예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다. 
#  따라서 12의 소인수는 2와 3입니다. 자연수 n이 매개변수로 주어질 때
#   n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요


# def solution(n):
#     answer = []    # 2, 3, 4, 6
#     answer2 = []
#     for i in range(2, n):
#         if n % i == 0:
#             answer.append(i)
    
#         for j in answer:
#             if j // i  == 1:
#                 answer2.append(j)
#     return answer2

# print(solution(12))

    
# 2 |12       3|15
# 2 |6          5
#   |3
# 모든 짝수는 소인수 2 포함

def solution(n):
    answer = [] 
    
    while n % 2 == 0:      # 짝수라면  // 홀수라면
        answer.append(2)   # answer리스트에 2를 일단 append한다 
        n //= 2            # 계속 2로 나눠준다 가장작은 홀수가 나올때까지
  
    for i in range(3, n + 1, 2):     
        #홀수라면 for문으로 들어온다(1,2는 계산할필요가 없으니까 3부터시작, +2를 해주며 홀수로만)
        while n % i == 0:   # n이 홀수로 나누어 떨어지면
            answer.append(i) # 홀수 i를 answer리스트에 append
            n //= i          
    
    answer = list(set(answer)) # 중복제거
    return sorted(answer)   #안했더니 통과 못하는 케이스 존재
print(solution(10000))


###############################################################
def solution(n):
    answer = []

    for i in range(2, n+1):
        while n % i == 0:
            if i not in answer:
                answer.append(i)
            n //= i
    return answer