#!/bin/python3

degree =[0,30,45,60,90]
sin = [0,1/2,0.70,0.86,1]
trigo = ["Sin","cos","tan","cot","sec","cosec"]
print("          ",end="")
for i in range(len(degree)):
    print(degree[i],end="           ")
print("\n")
for i in range(len(trigo)):
    print(trigo[i],end="")
    for j in range(len(sin)):
        if trigo[i] == "Sin":
            print("      ", sin[j],end="   ")
        elif trigo[i] == "cos":
            print("      ", sin[len(sin)-j-1],end="   ")
        elif trigo[i] =="tan":
            if sin[len(sin)-j-1] == 0:
                print("      ","ND",end="   ")
            else:
                print(f"      ", "{:.2f}".format(sin[j]/sin[len(sin)-j-1]),end="  ")
        elif trigo[i] == "cot":
                try:
                    if sin[j] == 1:
                        print(f"      ",sin[j],end="  ") 
                    else: 
                        print(f"      ", "{:.2f}".format(1/sin[j]/sin[len(sin)-j-1]),end="  ")
                except ZeroDivisionError:
                    print(f"      ","ND",end="  ")  

        elif trigo[i] == "sec":           
            try:
                print(f"      ", "{:.2f}".format(1/sin[len(sin)-j-1]),end="  ")
            except ZeroDivisionError:
                    print(f"      ","ND",end="  ")  

        else:
            try:
                print(f"      ", "{:.2f}".format(1/sin[j]),end="  ")
            except ZeroDivisionError:
                    print(f"      ","ND",end="  ")  
        
    print("\n")
