# 정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다.
#  배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.

# right은 리스트[-1]를 list[0]
# left는 리스트[0]을 list[-1]

# push, pop

# roatate함수

def solution(numbers, direction):
    
    if direction == "right":
        last_element = numbers[-1]
        for i in range(len(numbers) - 1, 0, -1):
            numbers[i] = numbers[i - 1]
        numbers[0] = last_element

    elif direction == "left":
        first_element = numbers[0]
        for i in range(len(numbers) - 1):
            numbers[i] = numbers[i + 1]
        numbers[-1] = first_element

    return numbers 

print(solution([1, 2, 3], "right"))
print(solution([4, 455, 6, 4, -1, 45, 6], "left"))

###################################################


def solution(numbers, direction):
    answer = []
    
    if direction == 'right':
        answer = numbers[-1:] + numbers[:-1]
    elif direction == 'left':
        answer = numbers[1:] + numbers[:1]
    
    return answer


#######################################################
큐 함수를 이용한 방법
from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)

appendleft : 왼쪽에 개체를 추가합니다.
extendleft : 왼쪽에 리스트를 연장합니다.
maxlen : 큐의 길이를 반환합니다.
popleft : 큐의 맨 왼쪽에 있는 개체를 반환합니다.
rotate : 큐를 회전합니다.