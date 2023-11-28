#  정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.

def solution(array):
    st = ''
    for i in array:
        st += str(i)
    answer = st.count('7')
    return answer
print(solution([7, 77, 17]))

###################################################
def solution(array):
    st = ''.join(map(str, array))
    answer = st.count("7")
    return answer

print(solution([7, 77, 17]))

##############################################

