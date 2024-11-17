score=float(input("enter your score(0-100)"))
if score>=0 and score<=100:
    if score>=90:
        print("you got grade A")
    elif score>=75:
        print("upu got grade B")
    elif score>=50:
        print("you got grade C")
    elif score>=35:
        print("you got grade D")
    else:
        print("you FAILED")
else:
    print("please enter a score between 0-100")