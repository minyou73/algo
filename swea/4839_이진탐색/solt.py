import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    P =  list(map(int, input().split()))
    A, B = list(map(int, input().split()))
    # 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb가
    left = 1
    right = P
    A_count = 0

    while True:
        center = int((left + right) / 2)

        # a의 목적페이지가 가운데보다 왼쪽에 있는경우/오른쪽 데이터 지우기
        if A < center:
            right = center
        # a의 목적페이지가 가운데보다 오른쪽에 있는 경우/왼쪽 데이터 지우기
        elif A > center:
            left = center
        # a의 목적페이지에 도달한 경우
        else:
            break

        A_count += 1

    left = 1
    right = Pa
    B_count = 0

     while True:
        center = int((left + right) / 2)

        # b의 목적페이지가 가운데보다 왼쪽에 있는경우/오른쪽 데이터 지우기
        if B < center:
            right = center
        # b의 목적페이지가 가운데보다 오른쪽에 있는 경우/왼쪽 데이터 지우기
        elif B > center:
            left = center
        # b의 목적페이지에 도달한 경우
        else:
            break

        B_count += 1
    
    
    print(f'#{tc} {})