# 한 마리당 쿠폰을 한 장 발급합니다. 쿠폰을 열 장 모으면 치킨을 한 마리 서비스로 받을 수 있고, 
# 서비스 치킨에도 쿠폰이 발급됩니다. 시켜먹은 치킨의 수 chicken이 매개변수로 주어질 때 
# 받을 수 있는 최대 서비스 치킨의 수를 return하도록 solution 함수를 완성해주세요.

# def solution(chicken):
#     coupon = 0
#     service_chicken = 0
#     left_coupon = 0
#     sum_coupon = []
#     answer = []
#     while chicken > 0:
#         coupon = chicken
#         service_chicken = chicken // 10
        
#         left_coupon = chicken - (service_chicken*10)
#         sum_coupon.append(left_coupon)
#         chicken = service_chicken
        
#         answer.append(service_chicken)
        
        
#         if sum(sum_coupon) == 10:
#             answer.append(1)
            

#     return sum(answer)

# # print(solution(1081)) # 테스트케이스 3, 9, 10 통과 안됨
# print(solution(1999)) #222


#################################################################
def solution(chicken):
    coupon = 0
    service_chicken = 0
    left_coupon = 0
    sum_coupon = []
    s_c = 0
    answer = []
    while chicken > 0:
        coupon = chicken
        service_chicken = chicken // 10
        
        left_coupon = coupon - (service_chicken*10)
        sum_coupon.append(left_coupon)
        chicken = service_chicken
        
        answer.append(service_chicken)
        
        s_c += left_coupon
        
    while s_c >= 10:
        service_chicken= s_c // 10
        answer.append(service_chicken)
        s_c = s_c - (service_chicken *10)
        s_c += service_chicken
        

    return sum(answer)

print(solution(1999)) #222