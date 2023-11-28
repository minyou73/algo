# my_string의 뒤의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.
# "grammerS123"

def solution(my_string, n):
    return my_string[-n:]


print(solution("ProgrammerS123", 11))