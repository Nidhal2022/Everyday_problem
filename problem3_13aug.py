def play_chess(min):
    t=min/20
    if min == 20:
        return f"Chef can play one time"
    elif min >20 :
        return f'Chef can play {t} times'
    elif min < 20:
        return f'Chef cant play chess'
print(play_chess(20))
print(play_chess(60))
print(play_chess(120))
print(play_chess(10))


