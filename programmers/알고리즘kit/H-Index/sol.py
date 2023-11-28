# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 
# 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
# [3, 0, 6, 1, 5]
# 이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다. 
# 그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다.

# https://www.ibric.org/bric/trend/bio-series.do?mode=series_view&newsArticleNo=8802417&articleNo=8882714&beforeMode=latest_list#!/list

# n=0 0번이상 인용 5개 // h의 범위는 최소 0번에서 최대 max(citations)가 될 수 있다
# n=1 1번이상 인용 4개
# n=2 2번이상 인용 3개
# n=3 3번이상 인용 3개 (정답)
# n=4 4번이상 인용 2개


def solution(citations):
    citations.sort()
    
    for h in range(len(citations)):
        answer = 0

        for j in citations:
            if j >= h:
                answer += 1 
        
        if answer == h:
            return h

print(solution([3, 0, 6, 1, 5]))

###################################################################

def solution(citations):
    citations.sort()
    article_count = len(citations)

    for i in range(article_count):
        if citations[i] >= article_count-i:
            return article_count-i
    return 0

    if citations[i] >= article_count-i:
    [0 , 1, 3, 5, 6]
    0  c[0] >= 5
    1  c[1] >= 4
    3  c[2] >= 3 *
    5  c[3] >= 2
    6  c[4] >= 1 
    
    최댓값을 찾아야 하므로 가장 큰 값부터 시작


    이중반복문으로 i인덱스 이상인 수를 카운트 해서 count_list에 넣기(H-index에 대한 이해부족)
    answer = []
    count_list = []
    
    for i in range(len(citations)):
        count = 0
        for j in range(len(citations)):
            if citations[j] >= citations[i]:
                count += 1
        count_list.append(count)

    for k in range(len(citations)):
        if count_list[k] >= citations[k]:
            answer.append((citations[k], count_list[k]))

    return max(answer)[0]




