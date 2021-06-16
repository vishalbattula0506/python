#1
##n=int(input("enter a number:"))
##c=0
##for i in range(1,n+1):
    ##if n%i==0:
        ##c+=1
##if c==2:
    ##print(n,"is a prime")
##else:
    ##print(n,"is not a prime")
      
#2
##n=int(input("enter a number:"))
##c=0
##for i in range(1,n+1):
    ##if n%i==0:
        ##c+=1
        ##print(i)
##if c==2:
    ##print(n,"is a prime")
##else:
    ##print(n,"is not a prime")

#3
##n=int(input('enter a number:'))
##c=0
##for i in range(1,(n//2)+1):
    ##if n%i==0:
        ##c+=1
##if c>1:
    ##print(n,'is not a prime number')
##else:
    ##print(n,'is a prime')

#4
##n=int(input('enter a number:'))
##import math
##s=int(math.sqrt(n))
##c=0
##for i in range(1,s+1):
##    if n%i==0:
##        c+=1
##if c>1:
##    print(n,'is not a prime')
##else:
##    print(n,'is a prime')
        
##def prime(n):
##    for i in range(2,n):
##        if n%i==0:
##            #print(n,'is not a prime')
##            break
##        else:
##            print(n,'is a prime')
##
##s=int(input('enter a number:'))
##e=int(input('enter a number:'))
##for i in range(s,e+1):
##    print(i)
##



##5
def prime(n):
    for i in range(2,n):
        if n%i==0:
            break
        else:
            print(n,'is a prime')

def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        else:
            return True


a=int(input('enter a number: '))
if prime(a):
    print(a,'is a prime')
while True:
    a+=1
    if prime(a):
        print(a,'is a prime')
        break
          

      
