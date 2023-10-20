import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    a = list(input())
    stack = []

    for i in a:
        if len(stack) == 0: # 비어있다면 append/ if not stack
            stack.append(i)
        else:

            if i == stack[-1]:    # i와 스택의 마지막 부분비교 
                stack.pop()                #같으면 pop
            else:               # 같지 않으면 
                stack.append(i)   #append
   


    print(f'#{tc} {len(stack)}')


