# 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다.
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록
#  solution 함수를 완성해주세요.

def solution(numbers):
    num = [i for i in range(10)]  # num = list[range(10)]
    numbers = sorted(numbers)
    answer = []
    
    for i in num:
        if i not in numbers:
            answer.append(i)
    
    return sum(answer)
  
print(solution([5,8,4,0,6,7,9]))


#######################################################
# set 사용해서 풀기?

def solution(numbers):
    a =  set(range(10)) - set(numbers)
    return sum(a) 

print(solution([5,8,4,0,6,7,9]))


#######################################################
# 와우..
# def solution(numbers):
#     answer = 45-sum(numbers)
#     return answer