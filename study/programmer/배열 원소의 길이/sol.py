# def solution(strlist):
#     answer = []
#     for i in strlist:
#         s = len(i)
#         answer.append(s)
#     return answer


# print(solution(["We", "are", "the", "world!"]))

def solution(strlist):
    answer = []
    for string in strlist:
        words = string.split()
        answer.append(len(words))
    return answer

print(solution(["We", "are", "the", "world!"]))