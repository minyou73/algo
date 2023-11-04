# 이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 
# 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.

# decimal_number = int(binary_string, 2)

def solution(bin1, bin2):
    dec1 = int("0b"+bin1, 2)
    dec2 = int("0b"+bin2, 2 )
    answer = bin(dec1+dec2)[2:]
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