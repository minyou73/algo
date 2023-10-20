import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) // 10

    memo = [0, 1, 3]

    while N >= len(memo):
        result = memo[len(memo)-2] * 2 + memo[len(memo)-1]
        memo.append(result)

    print(memo[N])
         # for t in range(1, T+1):
#     N = int(input())//10

#     memo = [1, 3]

#     if N > 2:
#         for i in range(2, N):
#             memo.append(memo[i-1] + memo[i-2]*2)

#     print(f'#{t} {memo[N-1]}')

# for tc in range(1, T + 1):
#     N = int(input())
#     memo = []
#     memo.append(1)
#     memo.append(3)
#         for i in range(2, N//10):
#             num = memo[i-1] + memo[i-2] * 2
#             memo.append(num)

#     print(f'#{tc} {memo[N]}')

