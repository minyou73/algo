# 머쓱이는 직육면체 모양의 상자를 하나 가지고 있는데 이 상자에 정육면체 모양의 주사위를 최대한 많이 채우고 싶습니다.
# 상자의 가로, 세로, 높이가 저장되어있는 배열 box와 주사위 모서리의 길이 정수 n이 매개변수로 주어졌을 때,
# 상자에 들어갈 수 있는 주사위의 최대 개수를 return 하도록 solution 함수를 완성해주세요

# box의 길이는 3입니다.
# box[0] = 상자의 가로, box[1] = 상자의 세로 box[2] = 상자의 높이 

# 직육면체의 가로, 세로, 높이를 각각 주사위값으로 나눈다
# 가로 * 세로 * 높이

def solution(box, n):
    answer = 0
    a = []
    for i in box:
        answer = i // n
        a.append(answer)

    answer2 = 1
    for j in a:
        answer2 *= j

    return answer2


print(solution([10, 8, 6], 3))

###################################################

def solution(box, n):
    width = box[0] // n
    length = box[1] // n
    height = box[2] // n 

    answer = width * length * height
    return answer

print(solution([10, 8, 6], 3))
