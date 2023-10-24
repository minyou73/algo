import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    
    #현재까지 합
    answer = 
    #열 방문 리스트
    visited = []
    f(0,0)


def f(index,sum):  # index: 현재 행의 값
    if index == N:
        answer = min(answer, sum)  #현재값과 더한 값중이 작은값 입력
        return

    for j in range(N):
        