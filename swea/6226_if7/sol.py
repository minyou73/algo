# 1~200 사이의 정수 가운데 7의 배수이면서 5의 배수는 아닌 모든 숫자들을 찾아

# 콤마(,)로 구분된 문자열을 구성해 출력하는 프로그램을 작성하십시오.

#T = range(1, 201)

#for t in T:
 #   if (t % 7 == 0) & (t % 5 != 0):
 #       s = str(t)
        
  #      print(s, end = ',')
         

         # numbers = list( map(  int,input().split() )  ) 
result = []

numbers = range(1, 201)
for num in numbers:
    if (num % 7 == 0) and (num % 5 != 0):
        result.append(str(num))

print(','.join(result))

