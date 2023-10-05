blood_list =[ 'A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

blood_dict = {
    'A' : 0,
    'B' : 0,
    'C' : 0,
    'D' : 0,
}

for blood in blood_list:
    blood_dict[blood] += 1

print(blood_dict)


########################################################

location_list = ['서울', '부산', '부산', '서울', '대전' ,'광주', '제주']

location_dict = {
    '서울': 1
}

for location in location_list:
    if location in location_dict.keys():
        location_dict[location] += 1
    else:
        location_dict[location] = 1

print(location_dict)