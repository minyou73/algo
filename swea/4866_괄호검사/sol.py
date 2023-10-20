import sys
sys.stdin = open('input.txt')
T= int(input())

for tc in range(T):
    string = input() # 입력받은 문자열
    result = 1
    stack = []

    for i in string:

        if i == '(' or i == '{':  # 스택이란 리스트에 (, {  여는 괄호 append해서 스택에 추가
            stack.append(i)
    
        elif i == ')' or i == '}':  # 닫는 괄호면 스택이 비어있으면 그냥 틀린거
            if not stack:
                result = 0
                break
        
            elif i == ')' and stack.pop() != '(':
                result = 0
                break
            elif i == '}' and stack.pop() != '{':
                result = 0
                break
            # 만약 닫는괄혼데 stack뒤랑 비교해서짝이 맞는지


    print(f'#{tc} {result}')