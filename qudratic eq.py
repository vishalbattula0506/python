#program to calculate the root of the quadratic equation
import cmath
a=4
b=3
c=6
d=(b**2)-(4*a*c)
root1=(-b+cmath.sqrt(d))/(2*a)
root2=(-b-cmath.sqrt(d))/(2*a)
print("the roots are {} and {}".format(root1,root2))
