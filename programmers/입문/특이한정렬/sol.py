# 정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다. 이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다.
# 정수가 담긴 배열 numlist와 정수 n이 주어질 때 numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.

# def solution(numlist, n):
#     minus = []

#     for i in numlist:
#         minus.append(abs(n - (i)))
    
#     di = {key:value for key, value in zip(numlist, minus) }
    
#     sorted_list = sorted(di.items(), key=lambda x: x[1])
#     sorted_dict = dict(sorted_list)

#     return sorted_dict  #{4: 0, 3: 1, 5: 1, 2: 2, 6: 2, 1: 3}


# print(solution([1, 2, 3, 4, 5, 6], 4))


# ######################################################################


# def solution(numlist, n):
#     minus = []

#     for i in numlist:
#         minus.append(abs(n - (i)))
    
#     li  = sorted(tuple(zip(minus, numlist)))
#     return li
#     # for j in li:
#     #     for k in li:
#     #         if j[0] == k[0]:
#     #             temp = j
#     #             j = k 
#     #             k = j
# print(solution([1, 2, 3, 4, 5, 6], 4))

# [(0, 4), (1, 5), (1, 3), (2, 6),(2, 2), (3, 1)]
##########################################################

def solution(numlist, n):
    minus = []

    for i in numlist:
        minus.append(abs(n - i))
    
    li = list(zip(numlist, minus))
    
    # 거리가 같을 경우 더 큰 숫자가 앞에 오도록 정렬
    li.sort(key=lambda x: (x[1], -x[0]))

    # 정렬된 숫자만을 반환
    result = [elem[0] for elem in li]
    return result

# 
print(solution([1, 2, 3, 4, 5, 6], 4))

#########################################################다른풀이
def solution(numlist, n):
    return sorted(numlist, key = lambda x : (abs(x-n), -x))

#########################################################

def solution(numlist, n):
    answer = []
    if n in numlist:
        answer.append(n)
    for i in range(1,10000):
        if n +i in numlist:
            answer.append(n +i)

        if n - i in numlist:
            answer.append(n -i)

    return answer
#########################################################

def solution(numlist, n):
    # num -> (abs(n-num), -num)
    numlist = [(abs(n-num), -num) for num in numlist]
    # 첫 번째 요소를 기준으로 오름차순 정렬 and 두 번째 요소를 기준으로 내림차순 정렬
    numlist.sort()
    # 두 번쨰 요소만 반환
    return [-num for _, num in numlist]