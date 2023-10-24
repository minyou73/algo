def solution(money):
    
    
    answer = []
    num = money // 5500 
    answer.append(num)
    el = money % 5500 
    answer.append(el)
    return answer


print(solution(5500))