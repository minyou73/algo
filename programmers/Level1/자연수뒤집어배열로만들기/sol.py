# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 
# 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.


# def solution(n):
#     a = []
#     for i in str(n):
#         a.append(int(i))
#     return sorted(a, reverse=True)
    

# print(solution(12345))

# 통과 안됨..


def solution(n):
    
    a = [int(i) for i in str(n)]
    return list(reversed(a))

print(solution(12345))

# 얘는 통과가 되네...? 무슨차이야..
