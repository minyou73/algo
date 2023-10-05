import sys
sys.stdin = open('input.txt')

T = int(input())        #int로 변환

for tc in range(1, T+1):    #1부터 시작해서 TC만큼//숫자받아옴
    char = input()          #한줄 받아오기 b 받아옴

    if char.islower():
        print(f'#{tc} {char} 는 소문자입니다.')
    else:
        print(f'#{tc} {char }는 대문자입니다.')