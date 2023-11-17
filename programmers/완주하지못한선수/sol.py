# 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 
# 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

def solution(participant, completion):
    my_hash = dict()

    for player1 in participant:
        if player1 in my_hash:
            my_hash[player1] += 1
        else:
            my_hash[player1] = 1

    for player2 in completion:
        my_hash[player2] -= 1

    for player, count in my_hash.items():
        if count > 0:
            return player

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))