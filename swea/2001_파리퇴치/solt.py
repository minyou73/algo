import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    matrix = []

    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    total = 0
# 파리채를 그리기 위한 기준점을 잡기위한 반복문
    for i in range(N-M+1):
        for j in range(N-M+1):
            
            temp = 0
            #파리채를 그리는 반복문 
            for row in range(M):
                for col in range(M):
                    temp += matrix[i+row][j+col]

            if total < temp:
                total = temp

    print(total)