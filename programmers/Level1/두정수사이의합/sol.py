# a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.


def solution(a, b):
    answer = 0
    if a < b: 
        for i in range(a, b+1):
            answer += i
    elif a == b:
        return a 
    elif a > b:
        for i in range(a, b-1, -1):
            answer += i
    return answer

print(solution(3,5))
print(solution(3,3))
print(solution(5,3))