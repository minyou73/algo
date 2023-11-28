def solution(numbers):
    
    answer = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)-1):
            multi  = numbers[i] * numbers[j]

            if answer < multi:
                answer = multi

    return answer

print(solution([1, 2, 3, 4, 5]))