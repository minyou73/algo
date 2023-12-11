# 3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에 3의 배수와 숫자 3을 사용하지 않습니다. 
# n을 3x 마을에서 사용하는 숫자로 바꿔 return하도록 solution 함수를 완성해주세요.
# 1	1 |	6	8
# 2	2 |	7	10
# 3	4 |	8	11
# 4	5 |	9	14
# 5	7 |	10	16


def solution(n):
    a = []
    for i in range(1, 250):
        if i % 3 != 0 and '3' not in str(i):
            a.append(i)

    answer = {}
    # answer = {key+1: value for key, value in enumerate(a)}

    for key, value in enumerate(a):
        answer[key+1] = value 

    return answer[n]
    
print(solution(15))


########################################################################
def solution(n):
    answer = 0
    count = 0
    while count < n:
        answer += 1
        if '3' in str(answer) or answer % 3 == 0:
            continue
        count += 1
    return answer

#####################################################################
def solution(n):
    x = [i for i in range(1, 200) if i % 3 != 0]
    y = [i for i in range(1, 200) if '3' not in str(i)]

    answer = list(set(x) & set(y))
    return answer[n-1]