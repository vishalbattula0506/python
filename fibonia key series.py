###1
##n=int(input('enter series range:'))
##a=0
##b=1
##print(a,end=' ')
##for i in range(2,n+1):
##    print(b,end=' ')
##    c=a+b
##    a=b
##    b=c


#2
n=int(input('enter series range:'))
a=0
b=1
print(a,b,end=' ')
for i in range(3,n+1):
    c=a+b
    a=b
    b=c
    print(b,end=' ')
    
