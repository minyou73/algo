# array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.

# n과 '-' [3, 10, 28] 그값이 가장 작은게 가장 가까운수
# array 배열안에 있는 값이 반환
# 3,  10  28
# 17, 10, 8


# def solution(array, n):
#     result = []
#     for i in array:                 # 3, 10 ,28 반환
#         result.append(abs(n - i))   # n인 20과의 차이를 절대값을 만들어 result배열에 append
        
#     ans = result.index(min(result))  # result의 최소값의 인덱스 반환
#     return array[ans]               # array 배열의 인덱스 반환
# print(solution([3, 10, 30], 20))

# 통과하지 못하는 케이스 존재
#############################################################################
# def solution(array, n):
#     result = []                     # 17, 10 ,10
#     sorted(array)
#     for i in array:                 # 3, 10 ,28 반환
#         result.append(abs(n - i))   # n인 20과의 차이를 절대값을 만들어 result배열에 append
   
#     min_val = (min(result))          # 17, 10 ,10 의 작은 값을 min_val(=10)에 넣는다
#     answer = result.count(min_val)   # result[17, 10, 10]에서 가장 작은값이 몇개인지 count한다
    
#     if answer >= 2:                 # 만약 count 값이 2 이상이면
#         return min(result)          #
   
# print(solution([3, 10, 30], 20))

###############################################################################
def solution(array, n):
    result = []                     # 17, 10 ,10
    array = sorted(array)           # sorted를 했기 때문에 알아서 더 작은 값이 반환
    for i in array:                 # 3, 10 ,28 반환
        result.append(abs(n - i))   # n인 20과의 차이를 절대값을 만들어 result배열에 append
   
    
    ans = result.index(min(result))  # result의 최소값의 인덱스 반환
    return array[ans]     

        
print(solution([3, 10, 30], 20))

###############################################################
def solution(array, n):
    answer = 100
    for num in array:
        if abs(num - n) < abs(answer - n):
            answer = num
        elif abs(num - n) == abs(answer - n):
            answer = min(num, answer)
    return answer

##############################################################
def solution(array, n):

    # array에 n을 넣고 sorted 한다음에 양옆의 값을 비교
    array.append(n)
    n_array = sorted(array)
    n_index = n_array.index(n)

    # n의 인덱스 값이 0 or -1 이면 1, -2 출력
    if n_index == 0:
        return n_array[1]

    elif n_index == len(n_array)-1:
        return n_array[-2]

    # n보다 작은수, n, n보다 큰 수를 비교해서 더 작은 값 출력
    else:
        if n_array[n_index+1] - n < n - n_array[n_index-1]:
            return n_array[n_index+1]

        # 작으면, n보다 작은 수 출력
        else:
            return n_array[n_index-1]