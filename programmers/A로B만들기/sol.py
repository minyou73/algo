# before의 순서를 바꾸어 after를 만들 수 있으면 1을, 
# 만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.

# def solution(before, after):
#     reverse_before = ''
#     for i in before[::-1]:
#         reverse_before += i

#     if reverse_before == after:
#         return 1
#     else:
#         return 0

# print(solution("olleh","hello"))
# print(solution("allpe", "apple"))

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

def solution(before, after):
    sort_bef = sorted(before)
    sort_aft = sorted(after)
    if sort_bef == sort_aft:
        return 1
    else:
        return 0
print(solution("olleh","hello"))