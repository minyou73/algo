# before의 순서를 바꾸어 after를 만들 수 있으면 1을, 
# 만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.

def solution(before, after):
    reverse_before = ''
    for i in before[::-1]:
        reverse_before += i

    if reverse_before == after:
        return 1
    else:
        return 0

print(solution("olleh","hello"))
print(solution("allpe", "apple"))

# 통과 못하는 케이스가 있었다.ㅜㅜ

########################################################################
# def solution(before, after):
#     before_list = list(before)
#     reversed_b_list = ''.join(reversed(before_list))
#     if reversed_b_list == after:
#         return 1
#     else:
#         return 0

# print(solution("olleh","hello"))

# 왜또 통과가 안될까...
########################################################################
# def solution(before, after):
#     
#     if before[::-1] == after:
#         return 1
#     else:
#         return 0

# print(solution("olleh","hello"))

######################################################################
# 문제를 잘못 이해했다 ;;;;;
# allpe의 순서를 바꿔도 apple 만들수없다.
# 알파벳이 다른 경우가 존재
# 정렬해서 두개가 똑같은지 비교하면 끝나는 문제다
def solution(before, after):
    sort_bef = sorted(before)
    sort_aft = sorted(after)
    if sort_bef == sort_aft:
        return 1
    else:
        return 0
print(solution("olleh","hello"))


################################################################
def solution(before, after):
    # before에 있는 문자열이 after에 있다면 
    for char in before:
        if char in after:
            # replace 이용해서 1개만 '0'으로 바꾸기
            before = before.replace(char, '0', 1)
            after = after.replace(char, '0', 1)

    # 반복문 종료 후 before와 after가 서로 같다면 문자열 내부 문자 갯수가 동일하단 의미
    if before == after:
        return 1
    else:
        return 0