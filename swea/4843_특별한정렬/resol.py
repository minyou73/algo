# 보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.
# N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.
# 예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
# 10 1 9 2 8 3 7 4 6 5
# 주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    big_sort = sorted(numbers, reverse=True)
    small_sort = sorted(numbers)

    answer = []

    for i in range(N):
        answer.append(big_sort[i])
        answer.append(small_sort[i])

    result = ''

    for j in range(10):
        result += str(answer[j]) + ' '

    print(f'#{tc} {result}')
