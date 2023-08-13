import random
cc=random.randint(1, 6)
cv=random.randint(1, 6)
def dice(c1,c2):
    
    if c1+c2>=6:
        return f'good turn, the roll {c1,c2} = {c1+c2}'
    else:
        return f'not good turn, the roll = {c1,c2} not equal to 6'

print(dice(cc,cv))