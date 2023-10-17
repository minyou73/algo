numbers = list(range(1, 5))

n= len(numbers)
# 모든 경우의 수 
for i in range(1<<n):   # 16번 반복 모든 부분집합
    # print(i)

    temp = []

    for j in range(n):  # 배열의 길이 만큼 [ 1, 2, 3, 4]
        # print(i, bin(i), bin(1<<j))
        if i & (1<<j):
            temp.append(numbers[j])

    print(temp)