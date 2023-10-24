import sys
sys.stdin = open('input.txt')

N, X = map(int, input().split()) 
number = list(map(int, input().split()))

for i in range(N):
    if X > number[i]:
        print(number[i], end='  ')