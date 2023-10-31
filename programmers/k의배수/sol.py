# 1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다. 
# 정수 i, j, k가 매개변수로 주어질 때, i부터 j까지 k가 몇 번 등장하는지 return 하도록 
# solution 함수를 완성해주세요.

# 리스트에 다 append 해서 '1'이라는 문자 세어주기?
# +=1

def solution(i, j, k):
    numbers = []
    for j in range(i, j+1):
        numbers.append(str(j))   #숫자를 문자로 바꿔서 리스트에 append
    
    num_num = ''.join(numbers)  # 12345678910111213
    
    result = 0
    for h in num_num:
        if h == str(k):      # 문자로 비교
            result += 1
    return result

print(solution(1, 13, 1))