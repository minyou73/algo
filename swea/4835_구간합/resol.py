import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))


    # a = [] append? 하기엔 너무 많아지지않나?
    # 이중 for문? 다섯개씩 반복- 
    # 규칙 n-m+1
    sum = 0
    for i in range(N-M+1):  

        for j in range(1, 1+M):
            sum += numbers[j]
        
        if 