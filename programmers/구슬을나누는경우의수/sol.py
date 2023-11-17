# 머쓱이가 갖고 있는 구슬의 개수 balls와 친구들에게 나누어 줄 구슬 개수 share이 매개변수로 주어질 때, 
# balls개의 구슬 중 share개의 구슬을 고르는 가능한 모든 경우의 수를 return 하는 solution 함수를 완성해주세요.

# import itertools

# def solution(balls, share):
#     ball_list = []
#     count = 0
#     for i in range(1,balls+1):
#         ball_list.append(i)
#     answer = list(itertools.combinations(ball_list,share))
#     for j in range(len(answer)):
#         count += 1
#     return count

# # print(solution(3, 2))
# print(solution(5, 3))

#시간초과

#########################################################

# import itertools

# def solution(balls, share):
#     ball_list = []
    
#     for i in range(1,balls+1):
#         ball_list.append(i)
#     answer = list(itertools.combinations(ball_list,share))
#     return len(answer)

# # print(solution(3, 2))
# print(solution(5, 3))

#시간초과


################################################################

# import math

# def solution(balls, share):
#     return math.comb(balls, share)

# print(solution(5, 3))

# ############################################################

# import itertools

# def solution(balls, share):
#     answer = list(itertools.combinations(range(1, balls+1), share))
#     return len(answer)

# print(solution(5, 3))

##########################################################3

# import math

# def solution(balls, share):
#     return math.factorial(balls) // (math.factorial(balls - share) * math.factorial(share))

########################################################################

# function solution(balls, share) {
#     // 둘이 같은 경우는 1 리턴
#     if (balls == share ) {
#         return 1;
#     }
    
#     // 분자의 경우, n!과 m!이 약분되는 것을 고려
#     let deno = 1;
#     for (let i = balls; i > share; i --) {
#         deno = deno * i;
#     }
    
#     // 분모의 경우, (n-m)!을 계산
#     let nume = 1;
#     for (let i = 1; i <= balls - share; i ++) {
#         nume = nume * i;
#     } 
    
#     // 둘을 나눌 때, 경우의 수는 정수로 출력되어야 함
#     return Math.round(deno / nume);
# }

########################################################################

def solution(balls, share):
    n = 1
    m = 1
    nm = 1
    answer = 0 

    for i in range(1, balls+1):
        n *= i 
    for j in range(1, share+1):
        m *= j
    for k in range(1, balls-share +1):
        nm *= k

    answer = n / (nm * m)
    return int(answer)

print(solution(5,3))

