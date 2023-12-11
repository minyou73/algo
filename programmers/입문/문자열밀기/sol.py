# 문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다. 
# 이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때, 
# A를 밀어서 B가 될 수 있다면 밀어야 하는 최소 횟수를 return하고 밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.


def solution(A, B):
    if A == B:
        return 0  # 이미 같은 문자열이면 이동할 필요 없음
    
    n = len(A)
    
    for i in range(1, n+1):
        rotated = A[-i:] + A[:-i]  # 문자열을 오른쪽으로 i 칸씩 이동
        if rotated == B:
            return i  # 이동한 횟수를 반환
    
    return -1  # 모든 이동을 시도한 후에도 B와 같아지지 않으면 -1 반환

# 예시
print(solution("hello", "ohell"))  # 1
print(solution("abcde", "eabcd"))  # 4
print(solution("abc", "bcd"))      # -1

A = A[-1] + A[:-1]
A[-1]: 리스트 A의 마지막 요소
A[:-1]: 리스트 A에서 마지막 요소를 제외한 모든 요소
rotated = A[-i:] + A[:-i]
A[-i:]: 리스트 A의 마지막에서부터 역순으로 i개의 요소를 선택합니다. 이는 리스트의 마지막 i개 요소를 나타냅니다.
A[:-i]: 리스트 A에서 마지막 요소를 제외한 모든 요소를 선택합니다. 이는 리스트의 처음부터 마지막에서 i개 요소를 제외한 부분을 나타냅니다.

##############################################################
from collections import deque

def solution(A, B):
    a, b = deque(A), deque(B)
    for cnt in range(0, len(A)):
        if a == b:
            return cnt
        a.rotate(1)
    return -1

print(solution("hello","ohell"))


##############################################################