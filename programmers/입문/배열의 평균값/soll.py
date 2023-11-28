def solution(numbers):
    
    sum = 0

    for i in numbers:
        sum += numbers

    a =  sum / len(numbers)
    
    return a



print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))