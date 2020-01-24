import random


def welcome():

    for i in range(0,20):
        print("$\t",end="")
    print()
    print("@",end="")
    for i in range(0,19):
        print("\t",end="")
    print("@")
    print("@",end="")
    for i in range(0,19):
        print("\t",end="")
    print("@")
    print("@",end="")
    for i in range(0,19):
        print("\t",end="")
    print("@")
    print("@",end="")
    for i in range (0,8):
        print("\t",end="")
    print("WELCOME",end="")
    for i in range(0,10):
        print("\t",end="")
    print("@")
    print("@",end="")
    for i in range(0,19):
        print("\t",end="")
    print("@")
    print("@",end="")
    for i in range(0,19):
        print("\t",end="")
    print("@")
    for i in range(0,20):
        print("$\t",end="")
    print()
    input("press any key to start")
def mainmenu():
    print("1.Rock papar scissors menu\n2.Cows and bulls menu \n3.Exit")
    ch=int(input("Enter your choice no.="))
    if ch==1:
        rockpaparscissorsmenu()
    elif ch==2:
        cowsandbullsmenu()
    elif ch==3:
        exit()
    else:
        print("invalid number")
        mainmenu()

def rockpaparscissorsmenu():
    print("1.Play\n2.Rules\n3.Return to main menu")
    ch = int(input("Enter your choice no.="))
    if ch == 1:
        rockpaparscissors()
    elif ch == 2:
        rockpaparscissorsrules()
    elif ch == 3:
        mainmenu()
    else:
        print("invalid number")
        rockpaparscissorsmenu()

def cowsandbullsmenu():
    print("1.Play\n2.Rules\n3.Return to main menu")
    ch = int(input("Enter your choice no.="))
    if ch == 1:
        cowsandbulls()
    elif ch == 2:
        cowsandbullsrules()
    elif ch == 3:
        mainmenu()
    else:
        print("invalid number")
        cowsandbullsmenu()

def rockpaparscissorsrules():
    print("1.Rock wins against scissors.\n2.Scissors win against paper.\n3.Paper wins against rock.")
    rockpaparscissorsmenu()

def cowsandbullsrules():
    print("On a sheet of paper, the players each write a 4-digit secret number. The digits must be all different. Then, in turn, the players try to guess their opponent's number who gives the number of matches. If the matching digits are in their right positions, they are bulls, if in different positions, they are cows.")
    cowsandbullsmenu()

def cowsandbulls():
    words=["rate","fail","cake","sore","tear","calm","rage","time","face","swan"]
    rand= random.randrange(0,10)
    word=words[rand]
    cnt=0
    while(cnt<15):
        s=input("enter string:")
        if s=="-1":
            print("thank you")
            break
        cows=0
        bulls=0
        chars=0
        for c in s:
            if c in word:
                chars+=1
        for i in range(0,4):
            if[i]==word[i]:
                bulls+=1
        cows=chars-bulls
        print("cows=",cows,"\tbulls=",bulls,)
        if bulls==4:
            print("congress! you win")
            mainmenu()
        cnt+=1
    print("oops max limit reach")
    mainmenu()

def rockpaparscissors():
    print("Welcome to rock papar scissors")
    print("you will compete against the computer")
    print(" the players score 5 point is winner")
    print("if your choice is rock enter 0")
    print("if your choice is papar enter 1")
    print("if your choice is scissors enter 2")
    print("if you exit the game enter -1")

    user=0
    comp=0
    cnt=0
    cho=["rock","papar","scissors"]
    while(user<5 and comp<5 and cnt<25):
        cnt+=1
        u_ch=int(input("enter your choice"))
        if u_ch==-1:
            print("thank you")
            break
        c_ch=random.choice([0,1,2])
        if u_ch==0 and c_ch==1:
            comp+=1
        elif u_ch==0 and c_ch==2:
            user+=1
        elif u_ch==1 and c_ch==0:
            user+=1
        elif u_ch==1 and c_ch==2:
            comp+=1
        elif u_ch==2 and c_ch==0:
            comp+=1
        elif u_ch==2 and c_ch==1:
            user+=1
        print("you=" ,cho[u_ch])
        print("computer",cho[c_ch])
        print("your score:", user,"\t comp score",comp)
    if (user>comp):
        print("congress! you win")
    elif(comp>user):
        print("oops! you lose")
    else:
        print("match draw")
    mainmenu()






welcome()
print("\n" * 100)
mainmenu()






















