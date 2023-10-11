def solution(numbers):
    
    
    numbers.sort(reverse = True)
    a = numbers[0]
    b = numbers[1]

    return a * b


print(solution([1, 2, 3, 4, 5]))


# numbers.sort()
# answer = numbers[-1] * numbers[-2]