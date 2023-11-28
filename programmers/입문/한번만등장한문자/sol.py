# s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요. 
# 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다

# hello 에서 중복된 문자 제거
# 마지막에 사전순으로 sort

def solution(s):
    answer = []
    for i in s:
        if i not in s:
            answer.append(i)
    return answer

print(solution("hello"))

# i는 이미 s 문자열 안에 있는 문자입니다. 따라서 이 코드는 아무런 문자도 answer에 추가하지 않습니다.
# count 해봐?

#############################################################

def solution(s):
    cnt= 0
    cnt_list = []
    
    for i in s:
        cnt = s.count(i)            # cnt.append(s.count(i)) -> [1, 1, 2, 2, 1]
        if cnt == 1:                # cnt 값이 1이라면
            cnt_list.append(i)      # cnt_list에 i값 append 해준다
    
    answer = ''.join(sorted(cnt_list)) # 정렬해서 eho 출력해준다
    return answer
    
print(solution("hello"))

###########################################################

def solution(s):
    answer = ''
    for i in s:
        if s.count(i)==1:
            answer += i
    return ''.join(sorted(answer))

###########################################################
def solution(s):
    answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
    return answer

##############################################
def solution(s):
    # s 안에 1개만 있는 문자만 stack에 추가
    stack = []
    for char in s:
        if s.count(char) == 1:
            stack.append(char)

        stack.sort() # 문자 순서대로 정렬
        return ''.join(stack) # 문자열로 출력 

    # 짧은버전
    stack = [char for char in s if s.count(char) == 1]
    stack.sort()
    return ''.join(stack)