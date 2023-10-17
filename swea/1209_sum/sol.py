import sys
sys.stdin = open('input.txt')

for i in range(10):
    N = int(input())

    matrix = []

    for i in range(100):
        numbers = list(map(int, input().split()))
        matrix.append(numbers)

    row_sum_list = []
    for i in range(len(matrix)):
        row_sum = 0
        for j in range(100):
            row_sum += matrix[i][j]
        row_sum_list.append(row_sum)

    col_sum_list = []
    for i in range(len(matrix)):
        col_sum = 0
        for j in range(100):
            col_sum += matrix[j][i]
        col_sum_list.append(col_sum)
    
    
    for i in range(100):
        diagnol = 0
        diagnol += matrix[i][i]

