# 머쓱이는 친구들과 369게임을 하고 있습니다. 369게임은 1부터 숫자를 하나씩 대며 
# 3, 6, 9가 들어가는 숫자는 숫자 대신 3, 6, 9의 개수만큼 박수를 치는 게임입니다. 
# 머쓱이가 말해야하는 숫자 order가 매개변수로 주어질 때, 
# 머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.

# 1부터 3,6,9게임  3,6,9나오면 박수치기
# 3의 배수가 아니라, 숫자 3, 6, 9의 개수대로 박수치기
# order=머쓱이가 말해야하는 숫자
# 머쓱이가 쳐야할 박수 횟수

def solution(order):
    orders = list(str(order))
    clap = 0
    
    for j in orders:
        if j == '3' or j == '6' or j == '9':
            clap += 1
    return clap

print(solution(29423))

#####################################################
def solution(order):
    clap_count = 0
    for digit in str(order):
        if digit in ['3', '6', '9']:
            clap_count += 1
    return clap_count