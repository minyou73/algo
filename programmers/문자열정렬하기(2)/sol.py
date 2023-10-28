# 영어 대소문자로 이루어진 문자열 my_string이 매개변수로 주어질 때,
#  my_string을 모두 소문자로 바꾸고 알파벳 순서대로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.

# 문자열 my_string을 for문으로 돌리며 하나씩 대문자인지 확인
# new_str이라는 빈 공간에 i가 대문자라면 소문자로 바꿔서 입력
# 소문자라면 그대로 입력
# s.sort()를 쓰면 안된다. - str type에 sort()라는 메소드가 없기 때문
# 대신 sorted(s)처럼 쓰는 것은 가능하다. - 대신 return type은 list이다.
# 이를 하나로 이어진 문자열로 만들기 위해선 ''.join을 사용하면 된다
# 출처 https://otugi.tistory.com/268

def solution(my_string):
    new_str = ''
    for i in my_string:
        if i.isupper():
            new_str += i.lower()
        else:
            new_str += i

    answer = ''.join(sorted(new_str))
    return answer

print(solution("Bcad"))

##############################################################
def solution(my_string):
    answer = ''
    for i in my_string:
        answer += i.lower()
    return ''.join(sorted(answer))

################################################################
def solution(my_string):
    return ''.join(sorted(my_string.lower()))