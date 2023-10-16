import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))
 
    total = 0

    for i in range(N):
        now = buildings[i]

        #현재 위치에 건물이 없다면 다음 건물로 이동
        if now == 0:
            continue
        #현재 위치에 건물이 있는 경우
        else:
            dx = [-2, -1, 1, 2]
            max_tall = 0

            #중심을 기준으로 네개의 건물중 가장 큰 건물 고르기
            for j in range(4):
                # i (now) : 현재위치(기준점)
                # dx[j] : 기준 건물을 중심으로 좌우 인덱스

                comp = buildings[i+dx[j]]

                if max_tall < comp:
                    max_tall = comp
            
            # 나머지 네개의 건물보다 현재 건물의 높이가 크다면 조망권 확보
            if now > max_tall:
                view = now - max_tall
                total += view

    print(f'{total}')



    print(N, buildings)