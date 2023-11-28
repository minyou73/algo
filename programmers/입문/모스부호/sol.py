# 문자열 letter가 매개변수로 주어질 때,
# letter를 영어 소문자로 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.
# letter의 모스부호는 공백으로 나누어져 있습니다.
# letter에 공백은 연속으로 두 개 이상 존재하지 않습니다.

# 딕셔너리로 replace?
# replace 함수는 문자열에 사용되는 메서드입니다


def solution(letter):
    answer = ''
    letter_list = letter.split()
    
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }

    for i in letter_list:
        answer += morse[i] 
        
    return answer

print(solution(".... . .-.. .-.. ---"))

########################################################################
def solution(letter):
    answer = ''
    letter = letter.split()
    for i in letter:
        answer += morse.get(i)
    return answer 
#########################################################################
return ''.join([morse[i] for i in letter.split(' ')])