#문자열 my_string이 매개변수로 주어질 때, my_string 안에 있는 숫자만 골라 
#오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.
#[1, 2, 2, 3, 9]

# my_string에서 숫자만 고르고 리스트 만들기
# 리스트 정렬

# isdigit( ): 어떤 문자열이 숫자의 형태면 True를 반환한다. 
# isnumeric( ): 숫자값 표현에 해당하는 문자열이면 True를 반환한다.

def solution(my_string):
    answer = []
    mylist = list(my_string)
    for i in mylist:
        if i.isdigit():
            answer.append(int(i))  #글자로 들어가서 오류나기 때문에 int형태로 바꾸어줘야한다

    answer.sort()

    return answer

print(solution("hi12392"))


#######################################################################
def solution(my_string):
    answer = []
    mylist = list(my_string)
    for i in mylist:
        if i.isdigit():
            answer.append(int(i))  #글자로 들어가서 오류나기 때문에 int형태로 바꾸어줘야한다

    answer.sort()

    return answer

########################################################################
import re

def solution(my_string):
    return sorted(map(int, (list(re.sub('[^0-9]', '', my_string)))))

def solution(my_string):
    return sorted(map(int, filter(lambda s: s.isdigit(), my_string)))