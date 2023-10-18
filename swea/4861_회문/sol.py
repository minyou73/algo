import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N_array = [list(map(int, input().split())) for _ in range(N)]
    matrix = [[0]* N for _ in range(N)]
    for nn in range(N):
        matrix[nn] = list(map(int,input().split()))
    result = 0
# N*N 배열 만들어서 입력
# 길이가 M인 배열
# 가로 세로 탐색
# 배열이 회문이면 회문결과 출력
arr = []
arr2 = []
result = []
for i in range(N):
    for j in range(N - M + 1):
        arr = []
        for k in range(M):
            arr.append(matrix[i][j + k])
        arr2 = arr[::-1]
        if arr == arr2:
            result.append(''.join(arr))
print(result)

# for i in range(N):  #r은 row c는 column
#         for j in range(N-M+1): 
#             if matrix[i][j:j+M] == matrix[i][j:j+M][::-1]: #회문이 맞는지 확인
#                 result.append(matrix[i][j:j+M]) 
#     print(result)
#             # for k in range(N-M+1) // 2):      # 0부터 문자열 길이의 절반만큼 반복
#             #     if word[i][j] != word[i][j+m-1-k ]:  

# for i in range(N-M+1):
#         for j in range(N):
#             for k in range(M):
#                 if matrix[i+k][j] = matrix[i+k][j][::-1]
#                     arr.append(matrix[i+k][j])
                