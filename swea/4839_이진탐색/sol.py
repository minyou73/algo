import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    P =  list(map(int, input().split()))
    Pa, Pb = list(map(int, input().split()))

    count_a = binary_search(P,Pa)
    count_b = binary_search(P,Pb)
    result = 0

    if count_a > count_b:
        result = B
        elif count_a < count_b:
            result = A
        else: 
            result = 0

print(f"#{tc} {result}")
    # 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb가


def binary_search(P,Page):
    start = 0
    end = P
    cen = int((left+right)/2) 
    count = 1
    
    while start <= end:
        mid = (start + end) // 2 # 중간값

        if mid == Page:
            return mid 		# target 위치 반환

        elif mid > Page: # target이 작으면 왼쪽을 더 탐색
            
        elif mid < Page:                     # target이 크면 오른쪽을 더 탐색 

        
        