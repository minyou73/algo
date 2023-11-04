# my_string에 나온 단어를 앞에서부터 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.

def solution(my_string):
    answer = list(my_string.split())
    return answer

print(solution(" i    love  you"))