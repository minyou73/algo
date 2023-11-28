# 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.

def solution(s1,s2):
    answer = []
    for i in s1:
        for j in s2:
            if i == j:
                answer.append(i)
    return len(answer)

print(solution(["a", "b", "c"],["com", "b", "d", "p", "c"]	))

#######################################################

def solution(s1, s2):
    return len(set(s1)&set(s2));

########################################################

def solution(s1, s2):
    dic = {i:1 for i in s1}
    answer = sum(dic.get(j,0)for j in s2)
    return answer