
import sys
sys.stdin = open('input.txt')
T = int(input())

# 도착한 지점에 충전기 있다(o)? -> 충전
# 도착한 지점에 충전기 없다(x)? -> 지나온길에 충전기 있으면 다시가서 충전 //

# K : 한번 충전으로 최대한 이동할 수 있는 정류장 수
# N : 종점 정류장
# M : 충전기가 설치된 정류장 개수
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charging_stations = list(map(int, input().split()))

    now = 0     # 현재 위치
    count = 0   # 몇번 충전하는지

    while now < N:
        # K만큼 더하면 바로 종점에 도착하는 경우, 반복문 종료
        if now + K >= N:
            break

            for i in charging_stations:
                if now <= i <= now + K:
                    now = i  # 충전기가 있는 정류장까지 이동
                    count += 1  # 충전 횟수 증가
                    break  # 충전기를 찾았으면 루프 종료

        # 충전기를 찾지 못하면, 충전기 설치가 잘못되어 종점에 도착할 수 없음
        else:
            count = 0
            break
    
    print(f'{tc} {count}')


##############################################################3

# # K만큼 이동하면서 충전기가 있는지 확인
#         for i in charging_stations:
#             if now <= i <= now + K:
#                 now = i  # 충전기가 있는 정류장까지 이동
#                 count += 1  # 충전 횟수 증가
#                 break  # 충전기를 찾았으면 루프 종료

###################################################################


