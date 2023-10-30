# num_list를 다음 설명과 같이 2차원 배열로 바꿔 return하도록 solution 함수를 완성해주세요.
# num_list가 [1, 2, 3, 4, 5, 6, 7, 8] 로 길이가 8이고 n이 2이므로 
# num_list를 2 * 4 배열로 다음과 같이 변경합니다. 
# 2차원으로 바꿀 때에는 num_list의 원소들을 앞에서부터 n개씩 나눠 2차원 배열로 변경합니다.

# num_list를 n으로 슬라이싱? 이차원배열 만들기

def solution(num_list, n):
    return [num_list[i:i+n] for i in range (0, len(num_list), n)]
    

print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))
print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948],3))

############################################################
# numpy 라이브러리가 있음

import numpy as np
def solution(num_list, n):
    li = np.array(num_list).reshape(-1,n)
    return li.tolist()