#---------------------#
# Libraries Summative #
#    Peyton Germann   #
#     Dec 9, 2022     #
#---------------------#
# im going to make slots
import rando, time
mon = 0

def time(n):
    from time import sleep
    sleep(n)
def attempt(c, c1, c2):
    x = 0
    x = c + 1
    if x == c1:
        x = 0
        x = c1 + 1
        if x == c2:
            x = 2500
            return x
    else:
        x = 0
        return x
print("Welcome to slots where you can gamble your life away.")
time(1)
print("No actual transaction occurs when you play this game.")
time(1)
print("In order to roll just push enter.")
time(1)
print("If you ever want to leave the program type 'x'")
time(1)

while True:
    total = rando.look()
    print(f"Your current total is ${total}")
    roll = input(" ")
    if roll == 'x':
        print("Bye")
        break
    else:
        w = 100
        while w > 0:
            x = rando.rando(0,9)
            x1 = rando.rando(0,9)
            x2 = rando.rando(0,9)
            print(f"{x}{x1}{x2}")
            w = w - 1
        p = 26
        while p > 0:
            print("")
            p = p - 1
        time(0.5)
        v, v1, v2 = rando.main()
        print(f"{v}{v1}{v2}")
        time(2)
        w = 100
        while w > 0:
            x = rando.rando(0,9)
            x1 = rando.rando(0,9)
            x2 = rando.rando(0,9)
            print(f"{x}{x1}{x2}")
            w = w - 1
        p = 26
        while p > 0:
            print("")
            p = p - 1
        mon = attempt(v, v1, v2)
        if mon == 2500:
            print("!!!!!!!!!!!!!!!")
            time(1)
            gud = rando.random_()
            print(gud)
            try:
                int(total)
            except:
                ValueError
            total = int(total) + mon
            print(f"Congrats you won ${mon}")
            time(2)
            mon = 0
        
        elif v == v1 and v1 == v2:
            print("!!!!!!!!!!!!!!!")
            time(1)
            gud = rando.random_()
            print(gud)
            if v <= 3:
                mon = 500
            elif v <= 6:
                mon = 1000
            elif v <= 8:
                mon = 5000
            elif v == 9:
                mon = 10000
            try:
                int(total)
            except:
                ValueError
            total = int(total) + mon
            print(f"Congrats you won ${mon}")
            time(2)
            mon = 0
        rando.writing(total)