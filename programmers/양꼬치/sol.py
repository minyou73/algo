# 머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다. 
# 양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다. 
# 양꼬치 n인분과 음료수 k개를 먹었다면 총얼마를 지불해야 하는지 return 하도록 solution 함수를 완성해보세요.
# n인분, 음료수 k개


# def solution(n, k):
#     if (n / 10) >= 1:
#         service = int(n /10) *2000

#     amount = (n * 12000)+ (2000 * k) - service
#     return amount
# print(solution(10,3))

# 런타임에러

###############################################


def solution(n, k):

    amount = (n * 12000)+ (2000 * k) - (int(n/10)*2000)
    return amount
    
print(solution(10,3))
