import random
import keyboard
q = []
w = []
e = []
r = []
temp = []
gene = [2,4]
lis = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
opt1 = [3,7,11,15]
opt2 = [12,8,4,0]
opt3 = [12,13,14,15]
opt4 = [0,1,2,3]
def gen():
    t = random.randint(0, 15)
    if 0 in lis:
        if lis[t] == 0:
            lis[t] = gene[random.randrange(len(gene))]
            return True
        elif lis[t] != 0:
            return True
            gen()
    else:
        print("You lose!")
        exit()
def matrix():
    q = lis[0:4]
    w = lis[4:8]
    e = lis[8:12]
    r = lis[12:16]
    print(str(q)  + "\n" + str(w) + "\n" + str(e) + "\n" + str(r) + "\n")
def left():
    for y in opt1:
        if lis[y] != 0:
            if lis[y] == lis[y-1] or lis[y-1]==0:
                lis[y-1] = int(lis[y-1]+lis[y])
                lis[y] = 0
        if lis[y-1] != 0:
            if lis[y-1] == lis[y-2] or lis[y-2]==0:
                lis[y-2] = int(lis[y-2]+lis[y-1])
                lis[y-1] = 0
        if lis[y-2] !=0:
            if lis[y-2] == lis[y-3] or lis[y-3]==0:
                lis[y-3] = int(lis[y-3]+lis[y-2])
                lis[y-2] = 0
def right():
    for y in opt2:
        if lis[y] != 0:
            if lis[y] == lis[y+1] or lis[y+1]==0:
                lis[y+1] = int(lis[y+1]+lis[y])
                lis[y] = 0
        if lis[y+1] != 0:
            if lis[y+1] == lis[y+2] or lis[y+2]==0:
                lis[y+2] = int(lis[y+2]+lis[y+1])
                lis[y+1] = 0
        if lis[y+2] !=0:
            if lis[y+2] == lis[y+3] or lis[y+3]==0:
                lis[y+3] = int(lis[y+3]+lis[y+2])
                lis[y+2] = 0
def up():
    for y in opt3:
        if lis[y] != 0:
            if lis[y] == lis[y-4] or lis[y-4]==0:
                lis[y-4] = int(lis[y-4]+lis[y])
                lis[y] = 0
        if lis[y-4] != 0:
            if lis[y-4] == lis[y-8] or lis[y-8]==0:
                lis[y-8] = int(lis[y-8]+lis[y-4])
                lis[y-4] = 0
        if lis[y-8] !=0:
            if lis[y-8] == lis[y-12] or lis[y-12]==0:
                lis[y-12] = int(lis[y-12]+lis[y-8])
                lis[y-8] = 0
def down():
    for y in opt4:
        if lis[y] != 0:
            if lis[y] == lis[y+4] or lis[y+4]==0:
                lis[y+4] = int(lis[y+4]+lis[y])
                lis[y] = 0
        if lis[y+4] != 0:
            if lis[y+4] == lis[y+8] or lis[y+8]==0:
                lis[y+8] = int(lis[y+8]+lis[y+4])
                lis[y+4] = 0
        if lis[y+8] !=0:
            if lis[y+8] == lis[y+12] or lis[y+12]==0:
                lis[y+12] = int(lis[y+12]+lis[y+8])
                lis[y+8] = 0
input("Welcome to 2048. Press enter to continue")
gen()
matrix()
di = input(": ")

while True:
    if di == 'l':
        left()
        left()
        left()
        gen()
        matrix()
    elif di == 'r':
        right()
        right()
        right()
        gen()
        matrix()
    elif di == 'd':
        down()
        down()
        down()
        gen()
        matrix()
    elif di == 'u':
        up()
        up()
        up()
        gen()
        matrix()
    di = input(": ")
# Warning: This code is very, very, very bad. It is just a quick version of 2048 I wrote in Python. I have no intention of optimizing it as I made this just for fun.
