# n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요.
#  답이 항상 존재함은 증명될 수 있습니다.

def solution(n):
    answer = []
    for i in range(1,n):
        if n % i == 1:
            answer.append(i)
    return min(answer)

print(solution(10))