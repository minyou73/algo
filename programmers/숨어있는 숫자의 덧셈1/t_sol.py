def solution(my_string):
    answer = 0

    for char in my_string:
        if char.isdigit():
            answer += int(char)

    return answer
    
    # for char in my_string:
    #     try:
    #         answer += int(char)
    #     except:
    #         continue


    # for char in my_string:
    #     if not (ord('A') <= ord(char) <= ord('z')):

    #     answer += int(char)



print(solution('aAb1B2cC34oOp'))