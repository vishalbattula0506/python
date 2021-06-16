n=int(input('enter a number:'))
s=int(input('enter a starting point:'))
e=int(input('enter end point:'))
for i in range(s,e+1):
   print(n,'*',i,'=',n*i)

n=int(input('enter a number:'))
s=int (input('enter a starting point:'))
e=int(input('enter end point:'))
while s<=e:
    print(n,'*',s,'=',n*s)
    s+=1
    
n=int(input('enter a number:'))
s=int (input('enter a starting point:'))
e=int(input('enter end point:'))    
for i in range(e,s-1,-1):
    print(n,'*',s,'=',n*i)

n=int(input('enter a number:'))
s=int (input('enter a starting point:'))
e=int(input('enter end point:'))
if s<e:
    for i in range(s,e+1):
        print(n,'*',i,'=',n*i)
