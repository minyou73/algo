def solution(num_list):
    num_list.reverse()    # num_list[::-1]
    print(num_list)

print(solution([1, 2, 3, 4, 5]))


def solution(num_list):
    answer = []

    for i in range(len(num_list)):
        # num_list[i] 
        # print(len(num_list-)i-1)    
        answer.append(num_list[len(num_list)-1-i]) #99에서부터 하나씩 빼면서

    for i in range(len(num_list)-1, 0, -1)



print(solution([1, 2, 3, 4, 5]))