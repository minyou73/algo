
# def solution(numbers):
#     m = []
#     for i in range(len(numbers)):
#         for j in range(i,len(numbers)):
#             multi = numbers[i] * numbers[j]
#             m.append(multi)
            
#     return max(m)


# print(solution([1, 2, -3, 4, -5]))



def solution(numbers):
    numbers.sort()
    
    answer = max(numbers[-1] * numbers[-2] , numbers[0] * numbers[1])
    return answer

print(solution([1, 2, -3, 4, -5]))

# def solution(numbers):
#     numbers.sort()
#     if numbers[0] * numbers[1] > numbers[-1] * numbers[-2]:
#         return numbers[0] * numbers[1]
#     else:
#         return numbers[-1] * numbers[-2]