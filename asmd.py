##def add(a,b):
##    print(a+b)
##def sub(a,b):
##    print(a-b)
##def mul(a,b):
##    print(a*b)
##def div(a,b):
##    print(a/b)
##
##a=int(input('enter a number: '))
##b=int(input('enter a number: '))
##add(a,b)
##sub(a,b)
##mul(a,b)
##div(a,b)


    
    
##def add(a,b):
##    print(a+b)
##def sub(a,b):
##    print(a-b)
##def mul(a,b):
##    print(a*b)
##def div(a,b):
##    print(a/b)
##
##a=int(input('enter a number: '))
##b=int(input('enter a number: '))
##c=int(input('enter a choice : '))
##
##if c==1:
##    add(a,b)
##elif c==2:
##    sub(a,b)
##elif c==3:
##    mul(a,b)
##else:
##    div(a,b)
##    

def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)

a=int(input('enter a number: '))
b=int(input('enter a number: '))
print('1:addition,2:substraction,3:multiplication,4:division')
c=int(input('enter a choice : '))

if c==1:
    add(a,b)
elif c==2:
    sub(a,b)
elif c==3:
    mul(a,b)
elif c==4:
    div(a,b)
else:
    print('INVALID')
