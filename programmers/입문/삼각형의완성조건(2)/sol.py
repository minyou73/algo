# 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다
# 삼각형의 두 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다.
# 나머지 한 변이 될 수 있는 정수의 개수를 return하도록 solution 함수를 완성해주세요.

# [3, 6]  6-3+1 <= 456/78  < 6+3
# [7, 11]  11-7+1  <=  5,6,7,8,9,10,11/12,13,14,15,16,17  < 7+11



def solution(sides):
    sides = sorted(sides, reverse=False) #[3, 6]
    a = sides[0]
    b = sides[-1]
    answer = []
    for i in range((b - a + 1), (a + b) ):
        answer.append(i)
    return len(answer)


print(solution([3, 6]))
print(solution([11, 7]))


####################################################################

def solution(sides):
    answer = []
    answer2 = []
    mn = min(sides)
    mx = max(sides)
    for a in range(mx-mn+1, mx+1):
        answer.append(a)
    for b in range(mx+1, mx+mn):
        answer2.append(b)
    return len(answer)+len(answer2)