a=int(input())
b=int(input())
c=b
while True:
    if c%a==0 and c%b==0:
        print('LCM of ',a,b,'is',c)
        break
    c+=1
