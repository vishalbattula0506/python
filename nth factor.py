##1

##n=int(input())
##f=int(input())
##c=0
##def fact(n,f,c):
##    for i in range(1,n//2+1):
##        if n%i==0:
##            c+=1
##            if c==f:
##                return i
##    else:
##        return 0
##    
##print(fact(n,f,c))        


##2(while loop)

##n=int(input())
##f=int(input())
##c=0
##i=1
##while f:
##    if n%i==0:
##        f-=1
##    if f==0:
##        print(i)
##        break
##    i+=1
##else:
##    print(0)
##    print()

##3(with recursion)

##n=int(input())
##f=int(input())
##c=0
##i=1
##a=f
##def fact(n,f,c,i):
##    if i>n:
##        return 0
##    if n%i==0:
##        c+=1
##        if c==f:
##            return i
##        else:
##            return fact(n,f,c,i+1)
##    else:
##        return fact(n,f,c,i+1)
##print(fact(n,f,c,i))
    
        
        
        
    
    
    




