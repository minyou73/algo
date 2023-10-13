
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    numbers = list(map(int, input().split()))

    min = 1000000
    min = numbers[0]
    max = 0
    max = numbers[0]

    for number in numbers:
        if min > number:
            min = number
        
        if max < number:
            max = number

    result = max - min
    print(f'#{tc}  {result}')