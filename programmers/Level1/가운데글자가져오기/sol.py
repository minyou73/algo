# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 
# 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

def solution(s):
    s_list = [i for i in s]
    if len(s) % 2 == 0:
        return ''.join([s_list[int((len(s)/2)-1)] , s_list[int(len(s)/2)] ])

    else:
        return s_list[int(len(s) / 2)]


# print(solution("abcde"))
print(solution("qwer"))

########################################################

def string_middle(str):
    return str[(len(str)-1)//2 : len(str)//2 + 1]

print(string_middle("power"))

#######################################################

def string_middle(str):
    a = len(str)
    if a % 2 == 0 :
        a = (a-2) / 2
    else :
        a = (a-1) / 2
    return str[int(a) : -int(a)]
print(string_middle("power"))
