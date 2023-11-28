#정수 배열 array가 매개변수로 주어질 때, 
#가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
#[8, 1]

#가장큰수 max함수사용해서 찾기/ index함수 사용해서 index값 찾기


def solution(array):
    answer = []
    a = max(array)
    answer.append(a)

    #array 배열에서 가장큰수인 a의 index값 찾기
    a_idx = array.index(a)
    answer.append(a_idx)
    
    return answer


print(solution([1, 8, 3]))