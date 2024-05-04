# Author: github.com/owaisahmedkhan725

# Calculator v-1.2
# Calculator
# Answers of All possible Calculation of given values at Once.
# This Update Fixes Error In Division Of Zero.

print()
print("                     Calculator                  ")

print ()
x=int(input("Enter Value 1: "))
y=int(input("Enter Value 2: "))

print()

a=x+y
print(x,"+",y,"=",a)

b=x-y
print(x,"-",y,"=",b)

c=x*y
print(x,"*",y,"=",c)

if (y!=0):
    d=x/y
    print(x,"/",y,"=",d)
else:
    print("Error Cannot Be Divided by Zero 0")

print()