import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = list(range(1, 13))
    N, K = list(map(int, input().split()))
    
    count = 0

    for i in range(1 << len(numbers)):   # 16번 반복 모든 부분집합
        temp = []
        
        for j in range(len(numbers)):  # 배열의 길이 만큼 [ 1, 2, 3, 4]
            if i & (1<<j):
                temp.append(numbers[j])

        if N == len(temp) and K == sum(temp):
            count += 1

    print(f'#{tc} {count}')