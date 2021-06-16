n=int(input('enter a number:'))
a=n
rev=0
while n:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
if rev==a:
    print(a,'is a palindrome')
else:
    print(a,'is not a palindrome')



n=int(input('enter a number:'))
if n==n[::-1]:
     print(n,'is a palindrome')
else:
    print(n,'is not a palindrome')
    
    
