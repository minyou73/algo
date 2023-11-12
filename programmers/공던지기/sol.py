# 머쓱이는 친구들과 동그랗게 서서 공 던지기 게임을 하고 있습니다. 
# 공은 1번부터 던지며 오른쪽으로 한 명을 건너뛰고 그다음 사람에게만 던질 수 있습니다. 
# 친구들의 번호가 들어있는 정수 배열 numbers와 정수 K가 주어질 때, 
# k번째로 공을 던지는 사람의 번호는 무엇인지 return 하도록 solution 함수를 완성해보세요.

# 친구들의 번호가들어있는 배열// k번쨰로 공을 던지는 사람의 번호?

# [1, 2, 3]| 1->3|3->1//총 개수 3개 홀수// 1-3만 왕복
# [1 ,2, 3, 4]| 1->3| 3->1 //총 개수 4개 짝수// 1-3만 왕복
# [1 ,2 ,3, 4, 5]|1->3|3->5|//총 개수 5개 홀수// 1 - 3- 5 왕복
# [1, 2, 3, 4, 5, 6]| 1 -> 3| 3->5|5->1|1 , 3, 5 반복//총 개수 6개 짝수

import math

def solution(numbers,k):
    n= int(math.ceil((2*k)/len(numbers)))
    answer = []

    for _ in range(n):    
        for i in numbers:
            answer.append(i)  # [1 2 3 4 5 6 1 2 3 4 5 6]  
    
    return answer[k*2-2]    


print(solution([1, 2, 3, 4, 5, 6],5))
# print(solution([1, 2, 3], 3))


# 1  2  3   4  5  6  1  2  3  4  5  6
# /     /      /     /     /     /
# 1     2      3     4     5
# [0]                     [8]   [10](5*2)


# 1  2  3  1  (2)  3  1  2  3
# /     /      /     
# [0]  [2]    [4]    [6]



#####################################################
def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]

#######################################################
from collections import deque

def solution(numbers, k):
    n = len(numbers) 일곱번째로 공을 던진 사람
    answer = [] # 3 1 3 1 3 1 3 1 3 1 3

    # 일단 deque를 써서 원형 큐를 만들어줍니다....
    circular_queue = deque(numbers)
    for i in range(k):
        # 두칸씩 미뤄줍시다... ( . . . 1 2 3 4 1 2 3 4 1 2 3 4 . . . )
        circular_queue.rotate(-2)
        answer.append(circular_queue[0]) # 3 1 3 1 3 1 3 1

    return answer[k-2]

print(solution([1, 2, 3, 4], 2)) #[3, 1]
print(solution([1, 2, 3, 4, 5, 6], 5))  # [3, 5, 1, 3, 5]
print(solution([1, 2, 3], 3))  # [3, 2, 1]