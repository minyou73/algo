# 영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다. 
# 영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때, 
# 영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.

# def solution(score):
#     answer=[]
#     avg = []
#     for x,y in score:
#         avg.append(int((x+y)/2))
    
#     sort_avg = sorted(avg, reverse=True)

#     di = {key:value+1 for value, key in enumerate(sort_avg)}
    

#     for a in avg:
#         if a == di.keys():
#             answer.append(di[0])
#     return answer


# print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
# 두번쨰 케이스 통과 못함
##############################################################################

# def solution(score):
#     answer = []
#     avg = []

#     for x, y in score:
#         avg.append(int((x + y) / 2))
    
#     sort_avg = sorted(avg, reverse=True)

#     di = {value: key + 1 for key, value in enumerate(sort_avg)}
#     # {75: 1, 70: 2, 65: 3, 55: 4}

#     for a in avg:
#         n = avg.count(a)
#         if n>=2 :
#             answer.append(di[a]-1)
#         else:
#             answer.append(di[a])

#     return answer

# # 예시
# # print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
# print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))
# # 1,3,6,7,8,9, 통과 못함
# 반례  [[1, 3], [3, 1], [2, 3], [3, 2], [1, 2], [1, 1]]

##########################################################################3

def solution(score):
    answer = []
    avg = []

    for x, y in score:
        avg.append(((x + y) / 2))
    
    sort_avg = sorted(avg, reverse=True)

    di = {value: key + 1 for key, value in enumerate(sort_avg)}
    # {75: 1, 70: 2, 65: 3, 55: 4}

    for a in avg:
        n = avg.count(a)
        if n==2 :               
            answer.append(di[a]-1)    
        elif n>2:
            answer.append(di[a]-n+1)
        else:
            answer.append(di[a])

    return answer

   

# print(solution( [[1, 3], [3, 1], [2, 3], [3, 2], [1, 2], [1, 1]])) // 소수
# print(solution([[1, 1], [0, 0], [2, 2]]))
print(solution([[80, 70], [70, 80], [50, 100], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))
# //공동등수 2명 이상


####################################################################3

def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]

#####################################################################3


def solution(score):
    rank = sorted([sum(s) / 2 for s in score], reverse=True)
    rankDict = {}
    for i, r in enumerate(rank):
        if r not in rankDict.keys():
            rankDict[r] = i + 1
    return [rankDict[sum(s) / 2] for s in score]


##############################################################################

def solution(scores):
    answer = []
    
    for i, score in enumerate(scores, start=1): #각 학생에게 1번부터 번호표 부착
        avg_score = sum(score) / len(score) #각 학생의 평균 계산(len(score)대신 2를 넣어도 됨.)
        
        rv_student = 0 # rv = Reference value(등수)

        for student in scores:
            rv_score = sum(student) / len(student) # 전체 평균을 구해서 rv_score 작성

            if rv_score > avg_score: # 학생 score가 평균보다 작으면
                rv_student += 1 # 등수를 하나 올려준다.(1등보다2등이 낮은 거임, 숫자가 올라갈수록 낮은 등수)

        answer.append(rv_student + 1)

    return answer