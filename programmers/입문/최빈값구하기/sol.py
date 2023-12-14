# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 
# 정수 배열 array가 매개변수로 주어질 때,최빈값을 return 하도록 solution 
# 최빈값이 여러 개면 -1을 return 합니다.


def solution(array):
    a = []
    for i in array:
        a.append(array.count(i))

    di = {key: value for key, value in zip(array, a)}
    max_count = max(di.values())

    if list(di.values()).count(max_count) > 1:
        return -1

    answer = [key for key, value in di.items() if value == max_count][0]
    
    return answer



# print(solution([1, 2, 3, 3, 3, 4]))
# print(solution([1]))
# print(solution([80,80,80,9,9]))
print(solution([1, 1, 2, 2]))

##############################################################################


def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1