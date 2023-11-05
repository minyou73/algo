# num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.

def solution(num_list):
    even_numbers = ''
    odd_numbers = ''

    for num in num_list:
        if num % 2 == 0:
            even_numbers += str(num)
        else:
            odd_numbers += str(num)

    return int(even_numbers) + int(odd_numbers)

# 예제 사용
print(solution([3, 4, 5, 2, 1]))