# Author: github.com/owaisahmedkhan725

# Calculator v-1.7
# Calculator Active+
# Support of Float Values
# Add Option to Exit Program After Execution of Operation
# Fix Unseen Answer Problem

while True:
    print('''
                    Calculator
      
 Choose a Number To Perform Action
      
 1.Addition     (+)
 2.Subtraction  (-)
 3.Multiply     (x)
 4.Dividision   (/)
 5.Percentage   (%)
 6.Square
 7.Modulus
 8.Increment
 9.Decrement
 
 ''')

    choice=int(input("Choose Your Operation : "))

    if choice in (1,2,3,4,5,7):
        x=float(input("Enter Value 1 : "))
        y=float(input("Enter Value 2 : "))
        
        if (choice == 1):
            Add = x+y
            print(x,"+",y,"=",Add)
        elif(choice == 2):
            Sub = x-y
            print(x,"-",y,"=",Sub)
        elif(choice == 3):
            Mul = x*y
            print(x,"*",y,"=",Mul)
        elif(choice == 4):

            if (y == 0):
                print("Error Cannot Be Divided by Zero 0")
            else:
                Div = x/y
                print(x,"/",y,"=",Div)

        elif (choice == 5):
            Perc = (x*y)/100
            print("Percentege of ",x,"%",y,"=",Perc)
        elif(choice == 7):
            Mod = x%y
            print(x,"Modulus",y,"=",Mod)

    elif choice in(6,8,9):

        x=float(input("Enter Value : "))

        if(choice == 6):
            Squ = x**2
            print("Square of ",x,"=",Squ) 
        elif(choice == 8):
            Inc = x+1
            print("Increment of ",x,"=",Inc)
        elif(choice == 9):    
            Dec = x-1
            print("Decrement of ",x,"=",Dec)
    else:
        print("You Choose Invalid Action")

    print()

    Ask_Exit=input("Do You Want To Exit Program Y/N : ")

    if(Ask_Exit=='y'):
        print('''
   Exiting...  
              ''')
        break;
    else:
        continue;