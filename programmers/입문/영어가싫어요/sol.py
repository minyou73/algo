# 영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 
# 문자열 numbers가 매개변수로 주어질 때, numbers를 정수로 바꿔 return 하도록 
# solution 함수를 완성해 주세요.


def solution(numbers):
    num = {
        'one' : 1 , 'two' : 2, 'three' : 3,
        'four' : 4, 'five' : 5, 'six' : 6,
        'seven' : 7, 'eight' : 8, 'nine': 9 
        'zero' : 0
    }

    answer = numbers  # 초기값 설정 초기값을 0으로 설정하면 문자열과 정수를 더할 때 혼동이 생길 수 있습니다.
    #  문자열에 정수를 더하려면 먼저 정수를 문자열로 변환해야 합니다.

#원소(키/값 쌍)들을 얻으려면 이름 뒤에 .items()를 쓰면 됩니다.
# dict_items([('one', '1'), ('two', '2') ... 튜플로 반환
# k에는 key 값, v에는 value값 할당

    for k, v in num.items():
        answer = answer.replace(k, str(v))
        # replace는 문자열을 변경하는 함수
    return int(answer)

print(solution("onefourzerosixseven"))

############################################################################

내 코드 효율적으로 줄인 경우(대충 머리가 나쁘면 돌아간다는 뜻)
def solution(numbers):
    r = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',\
         'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for k in r.keys():
        numbers = numbers.replace(k, r[k])
    return int(numbers)
#######################################################################
enumerate와 replace 사용한 함수
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)

####################################################################
def solution(numbers):
    # 인덱스 만들기(단어가 의미하는 숫자 = 인덱스)
    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for char in eng:
        if char in numbers:
            # 반복문으로 eng 내부 숫자가 포함되는지 확인하고 변환
           numbers = numbers.replace(char, str(eng.index(char)), numbers.count(char))
        
    return int(''.join(numbers))


        
