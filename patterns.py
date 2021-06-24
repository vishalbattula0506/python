#***
#***

##n=int(input())
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        print('*',end='')
##    print(end='\n')    


#*
#**

##n=int(input())
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print('*',end='')
##    print(end='\n')


#**
#*

  #01
##n=int(input())
##for i in range(n,0,-1):
##    for j in range(i,0,-1):
##        print('*',end='')
##    print(end='\n')

   #02
##n=int(input())
##for i in range(n,0,-1):
##    for j in range(1,i+1):
##        print('*',end='')
##    print(end='\n')
##

#  *
#* * *
#  *

##n=int(input())
##if n%2==1:
##    for i in range(1,n+1):
##        for j in range(1,n+1):
##            if i==n//2+1 or j==n//2+1:
##                 print('*',end=' ')
##            else:
##                print(' ',end=' ')
##        print()
##else:
##    print('wrong input')

    
#*****
#* * *
#*****
#* * *
#* * *

##n=int(input())
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i==1 or j==1 or j==n or i==n//2+1 or j==n//2+1:
##            print('*',end=' ')
##        else:
##            print(' ',end=' ')
##    print()


#    *
#   **
#  ***
# ****
#*****

##n=int(input())
##for i in range(1,n+1):
##    for k in range(1,n-i+1):
##        print(' ',end=' ')
##    for j in range(1,i+1):
##        print('*',end=' ')
##    print()

##    *****
##   *   *
##  *   *
## *   *
##*****

##n=int(input())
##for i in range(1,n+1):
##    for k in range(i,n):
##        print(' ',end=' ')
##    for j in range(1,n+1):
##        if i==1 or i==n or j==1 or j==n:
##            print('*',end=' ')
##        else:
##            print(' ',end=' ')
##    print()
##


##A
##AB
##ABC
##ABCD

  #01
##n=int(input())
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print(chr(64+j),end=' ')
##    print()    

   #02
##n=int(input())
##for i in range(65,65+n):
##    for j in range(65,i+1):
##        print(chr(j),end=" ")
##    print()

##A
##BC
##DEF
##GHIJ
##KLMNO

##n=int(input())
##c=65
##for i in range(65,65+n):
##    for j in range(65,i+1):
##        print(chr(j),end=" ")
##    print()

##ABCDE
##ABCD
##ABC
##AB
##A

##n=int(input())
##for i in range(n,0,-1):
##    for j in range(1,i+1):
##        print(chr(64+j),end=" ")
##    print()







