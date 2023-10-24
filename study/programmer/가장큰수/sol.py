from itertools import permutations

def solution(numbers):
    result = []
    for i in permutations(numbers,len(numbers)):
        result.append("".join(map(str,i)))
    return max(result)
print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))