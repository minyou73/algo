# start_num에서 end_num까지 1씩 감소하는 수들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

def solution(start, end_num):
    li = []
    for i in range(start, end_num - 1, -1):
        li.append(i)
    return li

print(solution(10, 3))