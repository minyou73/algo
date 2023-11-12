# 이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 
# 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.

# decimal_number = int(binary_string, 2)

def solution(bin1, bin2):
    dec1 = int("0b"+bin1, 2)   #10진수로 변환
    dec2 = int("0b"+bin2, 2 )
    answer = bin(dec1+dec2)[2:] #이진수로 변환 Ob 제외하기위해 [2:]
    return answer

print(solution("10", "11"))

#################################################
class Solution {
    public String solution(String bin1, String bin2) {
        int num1 = Integer.parseInt(bin1, 2);
        int num2 = Integer.parseInt(bin2, 2);
        int result = num1 + num2;
        String answer = Integer.toBinaryString(result);
        
        return answer;
    }
}


###############################################################
python 
def solution(bin1, bin2):
    # 내장함수 이용
    # return bin(int(bin1, 2) + int(bin2, 2))[2:]

    numbers = []
    number = int(bin1) + int(bin2)
    for num in str(number):
        numbers.append(int(num))
    
    for i in range(len(numbers)-1, 0, -1):
        while numbers[i] > 1:
            numbers[i] -= 2
            numbers[i-1] += 1
    if numbers[0] > 1:
        numbers[0] -= 2
        numbers.insert(0, 1)

    return ''.join(map(str, numbers))
