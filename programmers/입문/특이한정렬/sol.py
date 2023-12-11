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
    # 첫 번째 기준은 x[1]입니다. 즉, 두 번째 요소를 기준으로 정렬합니다. 기본적으로는 오름차순으로 정렬됩니다.
    # 두 번째 기준은 -x[0]입니다. 즉, 첫 번째 요소의 음수값을 기준으로 정렬합니다. 이는 두 번째 기준이 동일한 경우 큰 숫자가 먼저 오도록 하기 위함입니다.

    # 정렬된 숫자만을 반환
    result = [elem[0] for elem in li]
    return result

# 
print(solution([1, 2, 3, 4, 5, 6], 4))

#########################################################다른풀이
def solution(numlist, n):
    # numlist를 sort 후 
    # 딕셔너리 형태로 각 요소와의 차이를 적어서 절대값 처리
    # lambda 함수로 튜플 생성 후 key값 반환
    return sorted(numlist, key = lambda x: (abs(x - n), -x))

# 다른사람의 추가 설명
# key에 요소를 리스트 혹은 튜플로 두 개 이상 줄 수 있다. 
# 이 경우 앞에 값이 같을 때 뒤의 값을 이용해서 나열한다. 
# 요소 하나이고 값이 같을 때는 먼저 처리된 수가 먼저 나열되는 것 같다(인덱스가 작은 것이).

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

###############################################################3
    def solution(numlist, n):
    answer = []
    
    # numlist에 하나도 안남을때 까지 for문 반복
    while len(numlist) != 0:
        # val은 충분히 큰 숫자
        val = 100000    

        # n과의 거리 비교해서 더 작은 값을 val에 넣기
        for num in numlist:
            if abs(num-n) < abs(val-n):
                val = num

            # 만약 거리가 같다면 더 큰 수를 val에 넣기
            elif abs(num-n) == abs(val-n):
                val = max(val, num)

        # val을 answer에 넣고, numlist에서 제거하기
        answer.append(val)
        numlist.remove(val)

    return answer