s=int(input('enter a starting point:'))
e=int(input('enter an end point:'))
n=int(input('enter a number:'))
for i in range (s,e+1):
    if i%n==0:
        print(i,end='  ')
