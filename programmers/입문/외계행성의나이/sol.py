# 입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다.
# a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다. 
# 나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.

# for문으로 0~9까지 돌리면서 값을 입력.. 아닌가 index로 접근해야하나?
# 아스키코드?? a=97


def solution(age):
    change = []
    for i in str(age):    #age 숫자를 문자로 변환해서 하나씩 입력받고
        change.append(chr(int(i)+97))   #아스키코드 로 만들어서
    return ''.join(change)
print(solution(23))
print(solution(51))

###################################################
def solution(age):
    answer = ''
    alpha = {'0':'a', '1':'b', '2':'c', '3':'d', '4':'e', '5':'f',
            '6':'g', '7':'h', '8':'i', '9':'j'}
    
    for i in str(age):
        answer+=(alpha[i])
    return answer

    #########################################
    replace 함수 사용
    translate 함수