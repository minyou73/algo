# 한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 
# 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 같은 식이라면 가장 짧은 수식을 return 합니다.

def solution(polynomial):
    poly = polynomial.split("+")  #['3x ', ' 7 ', ' x']
    
    x = []                      # [3x , x]
    x_li = []
    number=[]

    for i in poly:              #poly의 공백제거
        i=i.strip()
        if "x" in i:            # poly에서 x가 들어있는 것만 고른다
            x.append(i)
        else:
            number.append(int(i))    # 상수항 리스트 

    for j in x:
        if j == "x":
            x_li.append(1)
        else:
            x_li.append(int(j.replace("x", "").strip())) # x를 공백으로 대체하고 숫자만
                                                         #strip 공백 문자 제거
  
  
    if str(sum(x_li)) == '1' and not number:
        return 'x'
    elif str(sum(x_li)) == '1':             # x가  1이라면
        return 'x' + ' + ' + str(sum(number))


    if not number:                                  # 상수가 비어있다면 x값만
        return str(sum(x_li)) + 'x' if sum(x_li) != 0 else '0'
    elif not x_li:                                  # x 값이 없다면 상수만
        return str(sum(number))
    else: 
        return str(sum(x_li)) + 'x' + ' + ' + str(sum(number))
   

print(solution("3x + 7 + x"))
print(solution("x + x + x"))
print(solution("1"))
print(solution("x+1"))
print(solution("x"))


# 8,10,12