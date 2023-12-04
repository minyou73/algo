#  머쓱이가 입력한 아이디와 패스워드가 담긴 배열 id_pw와 회원들의 정보가 담긴 2차원 배열 db가 
#  주어질 때, 다음과 같이 로그인 성공, 실패에 따른 메시지를 return하도록 solution 함수를 완성해주세요.
# 아이디와 비밀번호가 모두 일치하는 회원정보가 있으면 "login"을 return합니다.
# 로그인이 실패했을 때 아이디가 일치하는 회원이 없다면 “fail”를, 
# 아이디는 일치하지만 비밀번호가 일치하는 회원이 없다면 “wrong pw”를 return 합니다.

def solution(id_pw, db):
    
# my_list = [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]

# my_dict = {item[0]: item[1] for item in my_list}
# my_dict = dict(zip([item[0] for item in my_list], [item[1] for item in my_list]))

    db_dict = dict(db)
    if id_pw[0] in db_dict :
        if id_pw[1] in db_dict.values():
            return "login"
        else:
            return "wrong pw"
    else:
        return "fail"
    

print(solution( ["abc04", "345"], [["abc04", "335"], ["abc03", "345"]]))
통과 못함..
###############################################################################

def solution(id_pw, db):
    

    db_dict = dict(db)
    if id_pw[0] in db_dict :
        if id_pw[1] in db_dict[id_pw[0]]:
            return "login"
        else:
            return "wrong pw"
    else:
        return "fail"
    

print(solution( ["abc04", "345"], [["abc04", "335"], ["abc03", "345"]]))

#################################################################################

def solution(id_pw, db):
    answer = ''
    a, b = id_pw[0], id_pw[1]
    for pk, pw in db:
        if pk == a and pw == b:
            return "login"
    for pk, pw in db:
        if pk == a:
            return "wrong pw"

    return "fail"