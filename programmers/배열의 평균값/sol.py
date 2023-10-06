# def solution(*numbers):
#     result = numbers[0] 

#         for number in numbers:
#             sum += number
#             result.append(number)
#             return sum
            # sum / length.numbers


def solution(number):

    total = 0

    for number in numbers:
        total += number

    answer = total / len(numbers)
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))