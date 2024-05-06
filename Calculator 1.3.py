# Author: github.com/owaisahmedkhan725

# Calculator v-1.3
# Calculator
# Take Values And Perform Calculations as per the chosen action
# This Update Includes Choosing Actions.

print ()
x=int(input("Enter Value 1: "))
y=int(input("Enter Value 2: "))

print()

print ("Choose a number to perform Action")
print ("For + Press 1")
print ("For - Press 2")
print ("For * Press 3")
print ("For divide Press 4")

print ()
print ("Choice action above by Press 1 to 4")
print ()
z=int(input("Your Action = "))

if (z==1):
    a=x+y
    print(x,"+",y,"=",a)
elif(z==2):
    b=x-y
    print(x,"-",y,"=",b)
elif(z==3):
    c=x*y
    print(x,"*",y,"=",c)

elif(z==4):
    if (y==0):
        print("Error Cannot Be Divided by Zero 0")
    else:
        d=x/y
        print(x,"/",y,"=",d)
else:
    print("Invalid Action")

print()