import sys
sys.stdin = open('input.txt')

TC = int(input())

for i in range(TC):    # TC = 9
    num = int(input())       #항상 글자인 상태 숫자로 바꿔줘야


    if num % 2 == 1:
        print('홀수')
    else:
        print('짝수')
    

# #1차원 리스트 input 받기
numbers = input().split()
# print(numbers)
# print(type(numbers))

for number in numbers:
    int_num = int(number)    #글자 하나하나 int형으로 바꿔 int_num에 저장

    if int_num % 2 == 1:
        print(f'{int_num}은 홀수 입니다')


numbers = list( map(  int,input().split() )  )  # 아직 글자
# input.split 데이터를 하나씩 쪼갠다
# numbers = list( map(  int,['1','2','3','4','5'] )  )

# map int를 잘라진 '1','2' ... 하나씩에 적용


for number in numbers:
    if number % 2 == 1:
        print(f'{number}은 홀수입니다')
    else:
        print(f'{number}은 짝수입니다')



# 2차원 리스트 입력

N = int(input())
matrix = []

for i in range(N):
    numbers = list(map(int, input().split()))
    matrix.append(numbers)

print(matrix[2][0])
#데이터 자체를 반복
for row in matrix:
    for item in row:
        print(item)


# 행우선 반복 (index 접근)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(i, j, matrix[i][j])

# 열우선 반복(index 접근)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(j, i, matrix[j][i])