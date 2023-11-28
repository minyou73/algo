# 머쓱이는 큰 종이를 1 x 1 크기로 자르려고 합니다. 예를 들어 2 x 2 크기의 종이를 1 x 1 크기로 자르려면 
# 최소 가위질 세 번이 필요합니다. 최소로 가위질 해야하는 횟수를 return 

def solution(width, length):
    w = width - 1
    l = length - 1

    if width == 1 and length == 1:
        return 0
    elif width == 1:
        return l
    elif length == 1:
        return w
    else:
        return (w * length) + l

print(solution(2,2))

##############################################################
def solution(M, N):
    return (M * N) - 1