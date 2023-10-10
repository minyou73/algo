def solution(my_string, letter):
    answer = ''
    for string in my_string:
        if string != letter:
            answer += string

    return answer


print(solution("abcdef", "f"))



def solution(my_string, letter):
    answer = ''

    answer = my_string.replace(letter, '')
    return answer


print(solution("abcdef", "f"))



#리스트로 만들어서
#리무브
#조인으로 묶기

