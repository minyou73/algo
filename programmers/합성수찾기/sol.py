# 약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 
# 자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.
 
# 1의 약수 1/ 2의약수 1,2/ 3의 약수 1, 3/ 4의 약수 1, 2, 4/ 5의 약수 1,5
# 6의 약수 1, 2, 3, 6/ 7의 약수 1, 7/8의 약수 1, 2, 4, 8/ 9의 약수 1, 3, 9/ 
# 10의 약수 1, 2,5, 10

# 약수? 1부터 for문으로 돌리면서 숫자를 나눠서 나머지가 0 이나오면 약수

def solution(n):
    result = []
    for i in range(1, n+1): # 1~10까지 숫자 하나씩
        count = 0
        for j in range(1, n+1):
            if i % j == 0:  # i의 약수구하기
                count += 1     # i의 약수개수 구하기
        result.append(count)
    
    answer = 0
    for k in range(len(result)):
        if result[k] >= 3:
            answer += 1
    return answer

print(solution(10))