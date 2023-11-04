# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_list = []
    numbers = list(map(int, input().split()))

    max_value = max(numbers)
    min_value = min(numbers)
    answer = max_value - min_value

print(f'{tc} {answer}')
        