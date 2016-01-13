import random
if(input("please enter n ") == "n"):
    poss = ["H", "T"]
    chanses = int(input("choose the presenteces for H from "))
    if(chanses > -1 and chanses < 101):
        if (random.randint(1,100) <= chanses):
            print("H")
        else:
            print("T")
    elif (int(chanses) <= 0):
        print("T")
    elif (chanses >= 100):
        print("H")
