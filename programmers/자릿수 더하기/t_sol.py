# def solution(n):
    
    
#     while n > 0 :
#         # a는 몫 b는 나머지 저장
#         a = n // 10
#         b = n % 10

#         n = a
#         answer += b

def solution(n):
    for i in str(n):
        answer += int(i)

print(solution(1234))
print(solution(930211))