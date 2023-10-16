# import  sys
# sys.stdin = open('sample_input.txt')
# T = int(input())
# for tc in range(1, T+1):
#     # 기준값 뒤로 M개의 리스트 합 비교
#     numbers = list(map(int, input().split()))
#     n_list = list(map(int, input().split()))

#     sum_list = []
#     for i in range(0, numbers[0]-numbers[1]+1):
        
#         sum_list.append(sum(n_list[i:i+numbers[1]]))
#     print(f'#{tc} {max(sum_list) - min(sum_list)}')

    #구간합을 구하기 위한 i(시작점)/ 뒤에 m개의 데이터를 더하기 위한 시작점
    
    min_total = 100000000000000 
    max_total = 0
    
    for i in range(N-M+1):
        total = 0
    
        #시작점을 기준으로 오른쪽 M개의 숫자합
        for j in range(M):
            total += numbers[i+j]
        
        if total < min_total:
            min_total = total

        if total > max_total:
            max_total = total

    result = max_total - min_total

    print(f'{result}')