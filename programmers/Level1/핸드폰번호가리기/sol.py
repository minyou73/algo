# 전화번호가 문자열 phone_number로 주어졌을 때, 
# 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

# def solution(phone_number):
    
#     for i in range(0,len(phone_number)-4):
#         phone_number = phone_number.replace(phone_number[i],'*')
#     return phone_number
# print(solution("01033334444"))


#######################################################
def solution(phone_number):
    a = '*' * (len(phone_number) - 4)
    answer = a + phone_number[-4:]
    return answer

print(solution("01033334444"))
