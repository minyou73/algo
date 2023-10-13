
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # K : 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # N : 종점 정류장
    # M : 충전기가 설치된 정류장 개수
    k, n, m = list(map(int, input().split()))

    bus_stop = list(map(int, input().split()))
    count = 0
    now = 0

    # 충전할 필요가 없이 바로 도착한는 경우
    if k >= n:
        count = 0
    #충전을 하면서 지나가야하는 경우
    else:
        #버스가 아직 종점에 도착하지 않았다면 계속 반복
        while now < n:
            # 현재위치(now)기준으로 최대로 갈 수 있는 범위를 찾는다
            for i in range(now + k, now, -1):
                # 1. 최대범위가 종점을 넘는 경우
                if i >= n:
                    now = n
                    break
                # 2. 최대범위가 종점을 넘지 않은 경우
                if i in bus_stop:
                    now = i

                    count += 1
                    break
            #현재 위치에서 최대 거리까지 다 확인을 했는데 충전소가 없다면 도착 불가능
            else:
                count = 0
                now = n

    print(f'#{tc} {count}')
