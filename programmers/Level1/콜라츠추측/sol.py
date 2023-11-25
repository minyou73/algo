#  주어진 수가 1이 될 때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측입니다.
# 1-1. 입력된 수가 짝수라면 2로 나눕니다. 
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다. 
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다. 

# 6이라면 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 이 되어 총 8번 만에 1이 됩니다. 
# 몇 번이나 반복해야 하는지 반환하는 함수, solution을 완성
# 1인 경우에는 0을, 작업을 500번 반복할 때까지 1이 되지 않는다면 –1을 반환해 주세요


def solution(num):
    count = 0
    
    while num != 1:
        if count == 500:
            return -1   
        elif num == 1:
            return 0
        elif num % 2 == 0:
            num = num / 2
            count += 1
        elif num :
            num = num * 3 + 1
            count += 1
    return count
    
print(solution(6))
print(solution(16))
print(solution(626331))


########################################################
def solution(num):
    nums = []
    while num != 1:
        if num % 2 == 0:
            num = num // 2
            nums.append(num)
        else:
            num = num * 3 + 1
            nums.append(num)

    if len(nums) < 500:
        answer = len(nums)
    else:
        answer = -1
    return answer