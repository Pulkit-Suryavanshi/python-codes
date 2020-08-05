while True:
    enter = input("Enter the string")
    if(enter[-1]=="g"):
        if(enter[-2] =="n"):
            if(enter[-3] =="i"):
                print(enter+"ly")
    else:
        print(enter+"ing")
    enter2=input("y to continue e to exit\n")
    if(enter2=="y"):
        continue
    else:
        break