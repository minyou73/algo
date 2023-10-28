
# 머쓱이네 피자가게는 피자를 여섯 조각으로 잘라 줍니다.
#  피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, 
#  n명이 주문한 피자를 남기지 않고 모두 같은 수의 피자 조각을 먹어야 한다면 
#  최소 몇 판을 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요

# 6의배수   # n은 사람수
# 6*1,2,3.. / n == 0
# 몇판인지 알아야하니까 return i

def solution(n):
    pizza = 0
    for i in range(1,n+1):
        pizza = 6 * i
        if pizza % n == 0:
            return i

print(solution(6))
print(solution(10))
print(solution(4))

##################################################

def solution(n)
    pizza = 1
    while(pizza*6) % n != 0:
        pizza += 1
    return pizza