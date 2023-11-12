# my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 
# 문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.


def solution(my_string):
    my_string = my_string.split()
    answer = int(my_string[0])
    
    for i in range(len(my_string)):
     
        if my_string[i] == "+":
            answer += int(my_string[i+1])

        elif my_string[i] == "-":
            answer -= int(my_string[i+1])
        
            
    return answer

print(solution("3 + 4 - 2"))