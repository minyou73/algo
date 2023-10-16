import sys
sys.stdin = open('input.txt')

T = 10

for i in range(1,11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for a in range(dump):
        #최대높이
        max_box = boxes[0]
        max_idx = 0

        #최소높이
        min_box = boxes[0]
        min_idx = 0

        #최대와 최소 높이 찾기
        for a in range(len(boxes)):
            if max_box < boxes[i]:
                max_box = boxes[i]
                max_idx = i

            if min_box > boxes[i]:
                min_box = boxes[i]
                min_idx = i

        # max = max(boxes)
        # min = min(boxes)

        #평탄화
        boxes[max_idx] -= 1
        boxes[min_idx] += 1

        #전체 평탄화 횟수 전에 평탄화가 완료된 경우
        if boxes[max_idx] - boxes[min_idx] < 1:
            break


    result = max(boxes) - min(boxes)

    print(f'#{i} {result}')