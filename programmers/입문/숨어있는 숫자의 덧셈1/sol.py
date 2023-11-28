import re

def solution(my_string):
    sum = 0
    numbers = re.findall(r'\d', my_string)
    
    for i in numbers:
        sum += int(i)

    return sum




print(solution('aAb1B2cC34oOp'))


