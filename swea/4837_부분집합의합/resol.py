# 1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 
# 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
# 해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.

# 예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N,K = list(map(int, input().split()))  #N:원소개수 K:합
    A = list(range(1, 13))

    num = []
    sum_num = 0
    count = 0

    for i in range(0, len(A)-N +1):  #[10,11,12] 이상으로 넘어가지 않게
        num = A[i:i+N]              # A의 첫번쨰부터 N개까지 배ㅐ열을 잘라준다
        sum_num = sum(num)          # 잘라준 배열의 합을 구한다

        if sum_num == K:            # 배열의 합이 K와 같으면
           count +=1                # 개수를 세어준다
        # else:                     # 초기화 되어서 없애준다
        #     count = 0
            

    print(f'#{tc} {count}')


    #############################################################
import sys
from itertools import combinations
sys.stdin = open('input.txt')


T = int(input())
A = [i for i in range(1,13)]

for tc in range(1, T+1):
    # N : 부분집합 원소 수 , K: 부분집합의 합
    N, K = map(int, input().split()) 
    numbers = list(combinations(A, N))

    count  = 0
    for num in numbers:
        if sum(num) == K:
            count += 1

    print(f'#{tc} {count}')


