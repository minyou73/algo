# 정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 k가 있으면 
# num의 그 숫자가 있는 자리 수를 return하고 없으면 -1을 return 하도록 solution 함수를 완성해보세요

def solution(num, k):
 #Python에서는 문자열의 문자에 idx라는 속성이 없습니다. 
    result = []   
    str_num = list(str(num))  # 숫자열을 문자열로 변환하고 리스트를 만들어준다 [2, 9,1,8,3]
    answer = 0

    for i in range(len(str_num)): #i는 인덱스값//
        if str_num[i] == str(k):   #인덱스로 계산한 리스트값과 k 가 같으면 인덱스 반환
            return i+1             #자리수로 따지려면 1부터
    return -1
            

print(solution(29183, 1))

#############################################################
def solution(num, k):
    num = str(num)
    k = str(k)
    return -1 if k not in num else num.find(k)+1