#for i in range(1,11):
    #if i==20:
        #break
    #if i==20:
        #break
    #print(i,end='  ')
#else:
    #print('DONE')
    
n=int(input('enter a number:'))
for i in range(2,n):
    if n%i==0:
        print(n,'is not a prime')
        break
else:
    print(n,'is a prime')
