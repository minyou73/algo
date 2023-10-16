import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    max_sum = 0 
    min_sum = 99999999999

    for i in range(N-M+1):
        result = 0
        for j in range(i, i+M):
            result += numbers[j]

        if max_sum < result:
            max_sum = result
        
        if min_sum > result:
            min_sum = result

    
        answer = max_sum - min_sum

    print(f'#{tc} {answer}')
