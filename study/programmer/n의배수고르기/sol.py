
def solution(n, numlist):
    answer = []
    for i in numlist:         
        if i % n == 0:
            answer.append(i)
    return answer 
  
    # i for i in numlist:
        


print(solution(3, [4, 5, 6, 7, 8, 9, 10, 11, 12]))


# def solution(n, numlist):
#     for i in range(len(numlist)):
#         if numlist[i] % n != 0:
#             numlist.pop(i)
#         else: 
#             continue

#     return numlist