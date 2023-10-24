def solution(my_string):
    result = []
    for i in my_string:
        if i.isupper():
            i = i.lower()
            result.append(i)
        else:
            i = i.upper()
            result.append(i)

    return ''.join(result)
# 해당 문자열이 대문자로만 구성되어 있는지, 소문자로만 구성되어 있는지 알려주는 메소드입니다.
# swapcase() : 문자열에 있는 모든 문자의 대/소문자를 반대로 변환합니다.
# def solution(my_string):
#     result = ''
#     for i in my_string:
#         if i.isupper():
#             result += i.lower()
#         else:
#             result += i.upper()
#     return result

print(solution("cccCCC"))