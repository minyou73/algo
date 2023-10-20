import sys
sys.stdin = open('input.txt')
T= int(input())

for tc in range(T):
    code = input() # 입력받은 문자열
    stack = []

    for char in code:
        if char == '(' or  char == '{' :
            stack.append(char)

        elif len(stack) and char == ')' and stack[-1] == '(' :
            stack.pop()
        
        elif len(stack) and char == '}' and stack[-1] == '{':
            stack.pop()
        
        elif char == '}' or char == ')':
            stack.append(char)
          #짝이 안맞는 경우

    if len(stack) == 0:
        result = 1
    else:
        result = 0

    print(result)