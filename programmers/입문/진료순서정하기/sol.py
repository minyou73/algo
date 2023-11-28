#  응급도가 높은 순서대로 진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.

# 3 76 24 => 76  24 3 => 1 2 3
# 3,1,2       1  2  3
#            [0][1][2]
def solution(emergency):
    sort_emergency = sorted(emergency, reverse=True)  # 76, 24, 3
    answer = []                                       # [0] [1][2]

    for i in emergency:                 # 3, 76, 24
        # 3, 76, 24의 순서를 출력하려면        [2][0] [1]
        # i = sort_emergency.index(i)+1 # ==> 만약에 i=3 이면, 인덱스값[2]반환이니까 +1 해줘야한다
        
        change_index = sort_emergency.index(i)+1
        answer.append(change_index)
    return answer

print(solution([3, 76, 24]))

#######################################################
def solution(emergency):
    dict1={}
    list1=sorted(emergency,reverse=True)
    for i,x in enumerate(list1,start=1):
        dict1[x]=i
    answer=[dict1[x] for x in emergency]
    return answer
    print(solution([3, 76, 24]))