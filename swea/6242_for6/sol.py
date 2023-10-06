a=0
b=0
o=0
ab=0


data = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']


for d in data:
    if d == 'A':
        a = d.count('A')
    
    elif d == 'B':
        b = d.count('B')
    
    elif d == 'O':
        o = d.count('C')
        
    elif d == 'AB':
        ab = d.count('AB')
        

print(a)