def solution(angle):
    if 0 < angle <90:
        return 1
    elif 90 == angle:
        return 2
    elif 90 < angle < 180:
        return 3
    elif 180 == angle:
        return 4
    
print(solution(70))
print(solution(91))
print(solution(180))


def solution(angle):

#     answer = 0
# # if angle <90:
#     answer = -1