def solution(hp):

    a, b = divmod(hp, 5)
    hp = b
    answer += a

    a, b = divmod(hp, 3)
    hp = b
    answer += a

    answer += hp

    
    return answer



print(solution(23))   #5
print(solution(24))   #6
print(solution(999))