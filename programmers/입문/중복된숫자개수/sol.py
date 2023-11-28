# array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.

# def solution(array, n):
#     result = []
#     for element in array:
#         if element == n:
#             result.append(n)
    
#     return len(result)


# print(solution([1, 1, 2, 3, 4, 5], 1))

################################################################

def solution(array, n):
    c = array.count(n)
    return c

print(solution([1, 1, 2, 3, 4, 5], 1))