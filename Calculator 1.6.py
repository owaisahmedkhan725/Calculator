# Author: github.com/owaisahmedkhan725

# Calculator v-1.6
# Calculator Active
# User Friendly
# Short Code, Increase Code Readability And Efficiency
# Ask For Precise Action And Values
# Enhance Clutter and Reduce Numbers of Choices By Putting Action in Action

while True:
    print('''
                    Calculator
      
 Choose a Number To Perform Action
      
 1.Addition     (+)
 2.Subtraction  (-)
 3.Multiply     (x)
 4.Divide       (/)
 5.Percentage   (%)
 6.Square
 7.Modulus
 8.Increment
 9.Decrement
 
 ''')

    choice=int(input("Choose Your Operation : "))

    if choice in (1,2,3,4,5,7):
        x=int(input("Enter Value 1 : "))
        y=int(input("Enter Value 2 : "))
        
        if (choice == 1):
            add = x+y
            print(x,"+",y,"=",add)
        elif(choice == 2):
            sub = x-y
            print(x,"-",y,"=",sub)
        elif(choice == 3):
            mul = x*y
            print(x,"*",y,"=",mul)
        elif(choice == 4):

            if (y == 0):
                print("Error Cannot Be Divided by Zero 0")
            else:
                div = x/y
                print(x,"/",y,"=",div)
        elif (choice == 5):
            perc = (x*y)/100
            print("Percentege of ",x,"%",y,"=",perc)
        elif(choice == 7):
            mod = x%y
            print(x,"Modulus",y,"=",mod)
    elif choice in(6,8,9):
        x=int(input("Enter Value : "))

        if(choice == 6):
            squ = x**2
            print("Square of ",x,"=",squ) 
        elif(choice == 8):
            inc = x+1
            print("Increment of ",x,"=",inc)
        elif(choice == 9):    
            dec = x-1
            print("Decrement of ",x,"=",dec)
    else:
        print("You Choose Invalid Action")
        
    print()