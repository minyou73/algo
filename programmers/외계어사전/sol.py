# 알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수로 주어집니다. 
# spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1,
#  존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.

def solution(spell, dic):
    diction = {}

    for k, v in enumerate(dic, 1):
        count = 0
        for s in spell:
            count += v.count(s)
        diction[v] = count

    return diction

print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))




# def solution(spell, dic):
#     count = 0
#     diction = {d:0 for d in dic}  #{'def': 0, 'dww': 0, 'dzx': 0, 'loveaw': 0}

#     for i in range(len(spell)):   # spell [z,d,x]
#         for j in diction:         # diction에 있는 def, dww, dzx, loveaw 가져오기
#             if spell[i] in j:     # spell [z,d,x]가 def에 있다면, dww에 있다면
#                 diction[j] += 1   # diction의 value값 올려줌 하니씩
    
#     for k, v in diction.items():  # key, value 값 동시비교
#         if v == len(spell):       # value 가 한번씩 다 사용했다면
#             return 1
#     else:
#         return 2

# print(solution(["z", "d", "x"],["def", "dww", "dzx", "loveaw"]))
# # print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))


########################################################################

#....?? 
# ....ㅎ
# 어...이...가 .. 없네..?

def solution(spell, dic):
    for d in dic:
        if not set(spell) - set(d):
            return 1
    return 2
# print(solution(["z", "d", "x"],["def", "dww", "dzx", "loveaw"]))

####################################################################

