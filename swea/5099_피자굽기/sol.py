import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) #N 피자동시에구울수있는양 M입력받아온 피자개수
    cheese = list(map(int, input().split()))
    oven = []
    for i in range(M):
        oven.append([ cheese[i]])


    while len(oven) > 1:
        if oven[] // 2 == 0:
            oven.pop(0)
            if M < N:
                oven.append([cheese[M]])  
                
        else:
            pizza = oven.pop(0)
            pizza[1] //= 2
            oven.append(pizza)

   
    print(f"#{tc} {}")
        