# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수,
# solution을 작성해주세요.divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
        
    if len(answer) == 0:
        return [-1]
    
    return sorted(answer, reverse=False)
print(solution([5, 9, 7, 10], 5))
# print(solution([2, 36, 1, 3], 1))
# print(solution([3,2,6], 10))