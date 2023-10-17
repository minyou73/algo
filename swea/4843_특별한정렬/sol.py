# 배열 오름차순 정렬
# 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수
# list(n), list(0) list(n-1) list(0+1)
#10개의 데이터가 쌓일때까지
# 가장 큰수를 찾는다
# 가장 큰수를 새로운 배열에 넣는다
# 기존에 데이터에서 고른 숫자를 지운다

# 가장 작은수를 찾는다
# 가장 작은수를 새로운 배열에 넣는다
# 기존에 데이터에서 고른 숫자를 지운다

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N=int(input())
    numbers=list(map(int,input().split()))
    

    result = []

    while True:
        max_num = 0
        for i in range(len(numbers)):
            if max_num < numbers[i]:
                max_num = numbers[i]
        result.append(max_num)
        numbers.remove(max_num)

        min_num = 1000000000
        for j in range(len(numbers)):
            if numbers[j] < min_num:
                min_num = numbers[j]
        result.append(min_num)
        numbers.remove(min_num)

        if len(result) == 10:
            break

    temp = list(map(str, result))
    result = ' '.join(temp)
    print(f'#{tc}{result}')
