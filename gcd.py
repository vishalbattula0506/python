a=int(input())
b=int(input())
if a>b:
    a,b=b,a
for i in range(b,0,-1):
    if a%i==0 and b%i==0:
        print('gcd of',a,b,'is',i)
        break
