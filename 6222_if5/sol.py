import sys
sys.stdin = open('input.txt')

P = input()


if P.islower():
    print(f'{P}(ASCII: {ord(P)}) => {P.upper()}(ASCII: {ord(P.upper())})')

elif P.isupper():
    print(f'{P}(ASCII: {ord(P)}) => {P.lower()}(ASCII: {ord(P.lower())})')

else:
    print(P)



#if P.islower():
#    result = P.upper()
#else:
#    result = P.lower()

# print(ord(char), ord(result))    
# if P.isalpha()