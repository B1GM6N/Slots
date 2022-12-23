# library for getting a random number
good = ("AMAZING!", 'SPECTACULAR', 'WOW', "AWESOME", ":)")
import random

def rando(mi,ma):
    random_num = random.randint(mi, ma)
    return random_num
def random_():
    ra = random.choice(good)
    return ra

def look():
    file = open('cash.txt', 'r')
    red = file.read()
    file.close()
    return red

def writing(current):
    file = open('cash.txt', 'w')
    file.write(f"{current}")
    file.close()
# gets the slot value
def main():
    a = rando(0, 9)
    b = rando(0, 9)
    c = rando(0, 9)
    return a, b, c


        
    
    