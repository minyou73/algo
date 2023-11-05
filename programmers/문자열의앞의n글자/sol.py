# my_string의 앞의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.

def solution(my_string, n):
    answer = []
    for i in range(0, n):
        answer.append(my_string[i])
    return ''.join(answer)


print(solution("ProgrammerS123", 11))