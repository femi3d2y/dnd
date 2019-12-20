import random

def die_100():
    ls = []
    for n in range(0,91,10):

        ls.append(n) 

    roll = random.choice(ls)  

    return roll

def die_10():
    
    roll = random.randint(0,9)

    return roll

print(die_100()+die_10())