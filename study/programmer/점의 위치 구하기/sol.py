def solution(dot):
    x = dot[0]
    y = dot[1]
    if x > 0 and y > 0:
        answer = 1
    elif x < 0 and y > 0:
        answer = 2
    elif x < 0 and y < 0:
        answer = 3
    elif x >0 and y < 0 :
        answer = 4
    
    
    return answer

print(solution([2, 4]))