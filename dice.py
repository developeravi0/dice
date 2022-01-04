#dice simulator
import random
def dice():
    print("Activated dice roll simulator")
    no1="""
            [   ]
            [ 0 ]
            [   ]
    """
    no2="""
            [0  ]
            [   ]
            [  0]
    """
    no3="""
            [0  ]
            [ 0 ]
            [  0]
    """
    no4="""
            [0 0]
            [   ]
            [0 0]
    """
    no5="""
            [0 0]
            [ 0 ]
            [0 0]
    """
    no6="""
            [000]
            [000]
            [000]
    """
    while True:
        dice=random.randint(1,6)
        print(f"The dice rolled the number {dice}.")
        if dice==1:
            print(no1)
        elif dice==2:
            print(no2)
        elif dice==3:
            print(no3)
        elif dice==4:
            print(no4)
        elif dice==5:
            print(no5)
        else:
            print(no6)
        yn=str(input("Do yo want to roll the dice again (y/n) : "))
        if yn=="n":
            print("Exited dice roll simulator")
            break
if __name__=="__main__":
    dice()