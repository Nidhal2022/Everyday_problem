
def chef_left(min):
    if min == 30:
        return "Reach exactly on time"
    elif min >30 :
        return f'chef will reach{min-30}  minutes early'
    elif min < 30:
        return f'Chef late for {30-min} minutes'
    
print(chef_left(30))
print(chef_left(60))
print(chef_left(14))
