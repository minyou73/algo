import sys
sys.stdin = open('input.txt')
T= int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = []

    for _ in range(N):
        matrix.append(input())
        # matrix.append(list(input()))
    
    result = ''
    # 가로 기준점 / 회문의 시작점을 잡기위한 반복문
    for i in range(N):
        for j in range(N-M+1):

            for row in range(M):
                #front : 맨앞글자부터 한칸씩 증가
                f = matrix[i][j+row]
                #back: 맨뒷글자부터 한칸씩 감소
                b = matrix[i][j+M-1-row]

                #앞뒤 동일
                if f == b:
                    continue
                #앞뒤 다르다면
                else:
                    break
            #break만나지 않은 경우 - 끝까지 반복하고 회문찾은경우
            else:
                for a in range(M):
                    result += matrix[i][j+a]
    
    
    #세로 기준점/ 회문의 시작점을 잡기
    for j in range(N):
        for i in range(N-M+1):
            for col in range(M//2):
                f = matrix[i+col][j]
                b = matrix[i+M-1-col][j]    

                if f == b:
                    continue
                else:
                    break

            else:
                for a in range(M):
                    result += matrix[i+a][j]    
    
    
    
    
    print(result)
