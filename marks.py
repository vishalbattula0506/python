m=int(input("ENTER MARKS"))
if m>=0 and m<=100:

    if m>=80:
        print("A GRADE")
    elif m>=60 and m<80:
        print("B GRADE")
    elif m>=40 and m<60:
        print("C GRADE")
    else:
        print("FAIL")

else :
    print("INVALID INPUT")

        
    
