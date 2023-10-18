import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N_array = [list(map(int, input().split())) for _ in range(N)]
    N_array = [[0]* N for _ in range(N)]
    for nn in range(N):
        N_array[nn] = list(map(int,input().split()))
    result = 0
 #N*N배열
 #M*M배열
    fly = []
 #N*N 배열에 M*M부분만큼 더하기
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for k in range(M):
                for l in range(M):
                    total += N_array[i+k][j+l]
                    fly.append(total)

    max_ = max(fly)

    print(max_)