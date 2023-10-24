def solution(num_list):
    even = 0
    odd = 0
    
    for i in num_list:
        if i % 2 == 0 :
            even += 1
            
        else:
            odd += 1
    
    answer = [even, odd]
    return answer


print(solution([1, 2, 3, 4, 5]))