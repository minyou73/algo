import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    #V = 노드수, E = 간선수 
    V, E = list(map(int, input().split()))

    nodes = [[0 for _ in range(V+1)] for _ in range(V+1)]  #그래프표현(인접행렬)

    for _ in range(E):
        node = list(map(int, input().split()))
        start = node[0]
        end = node[1]

        nodes[start][end] = 1


    S, G = list(map(int, input().split()))

    #방문 체크리스트
    check_list = [False] * (V+1)

    #dfs용 stack
    stack = []

    #V부터 시작
    v = S 
    check_list[v] = True
    stack.append(v)

    while len(stack):
        for w in range(V+1):
            #연결된것을 확인 ==1인지 확인
            if nodes[v][w] == 1:
                #아직 방문하지 않았다면 / 체크리시트에 false라면
                if not check_list[w]:
                    #현재위치 v를 stack에 push
                    stack.append(v)
                    check_list[w] = True

                    #w를 현재 위치로 변경
                    v = w

                    if w == G:
                        result = 1
                    
                    break
        # break 만나지 않은경우 - 방문하지 않은 정점이 없는 경우 / 과거의 위치로 돌아가기
        else:
            v = stack.pop()

