# 문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요
# abc/def1/23
# 012/345/678

def solution(my_str, n):
    list_my_str = list(my_str)
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(my_str[:n])
        my_str = my_str[n:] 
    return answer



print(solution("abcdef123", 3))
#################################################################
def solution(my_str, n):
    result = []

    for i in range(0, len(my_str), n):
        result.append(my_str[i:i + n])

    return result

################################################################        
def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0, len(my_str),n)]

#############################################################33
