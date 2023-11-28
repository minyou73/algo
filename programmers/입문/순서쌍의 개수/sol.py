def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += 1
    
        
    return answer




print(solution(20))

# 곱이 20인 순서쌍은 (1, 20), (2, 10), (4, 5), (5, 4), (10, 2), (20, 1) 이므로 6을 return합니다

def solution(n):
    answer = 0
    for num in range(1, int(n ** 0.5)+1)
        if n % i == 0:
            answer += 2

        if num * num == n:
            aswer -= 1
    
        
    return answer




print(solution(20))