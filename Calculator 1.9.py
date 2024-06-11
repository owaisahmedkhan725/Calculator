# Author: github.com/owaisahmedkhan725

# Calculator v-1.9
# Advance Calculator
    #include
        # Calculator   //IMPORT FROM Calculator 1.8.py (Merge)
        # Converter    //Including Converter Option (Unit Conversion)
# Coverters Includes
# 1.Hours to Sec
# 2.Sec To Hours
                      
# To be Construct  //Continue... 

import math

while True:
    print('''Advance Calculator + Converter
    Choose Your Option by Pressing
    1. Calculator
    2. UnitConverter
    3. Exit
          ''')
    
    i=int(input("Your Choice : "))
    if i==1:

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
 7.Root
 8.Power
 9.Factorial
 10.Modulus
 11.Increment
 12.Decrement
 13.Exit
 ''')

            choice_Operation=int(input("Choose Your Operation : "))

            if choice_Operation in (1,2,3,4,5,10):
                x=float(input("Enter Value 1 : "))
                y=float(input("Enter Value 2 : "))
                print()

                if (choice_Operation == 1):
                    Add = x+y
                    print(x,"+",y,"=",Add)

                elif(choice_Operation == 2):
                    Sub = x-y
                    print(x,"-",y,"=",Sub)

                elif(choice_Operation == 3):
                    Mul = x*y
                    print(x,"*",y,"=",Mul)

                elif(choice_Operation == 4):

                    if (y == 0):
                        print("Error: Zero(0) Cannot Be Divisior")
                    else:
                        Div = x/y
                        print(x,"/",y,"=",Div)

                elif (choice_Operation == 5):
                    Perc = (x*y)/100
                    print("Percentege of ",x,"%",y,"=",Perc)

                elif(choice_Operation == 10):
                    Mod = x%y
                    print(x,"Modulus",y,"=",Mod)

            elif choice_Operation ==8:

                x=int(input("Enter Value : "))
                y=int(input("Enter Power Value ^ : "))
                
                print()

                Power=x**y
                print(x,"^",y,"=",Power)
                
            elif choice_Operation in(6,7,9,11,12):

                x=float(input("Enter Value : "))
                print()

                if(choice_Operation == 6):
                    Squ = x**2
                    print("Square of ",x,"=",Squ)

                elif(choice_Operation==7):
                    if (x<0):
                        print("Error: Cannot Calculate Root of Negative Number")
                    else:
                        Root= math.sqrt(x)
                        print(Root)

                elif(choice_Operation==9):
                    if x<0:
                        print("Error: Cannot Calculate Factorial of a Negative Number")
                    elif x==0:
                        print("Factorial of 0 is 1")
                    else:
                        Factorial=1
                        i=1
                        while i<=x:
                            Factorial=Factorial*i
                            i+=1
                        print("Factorial of",x, "is",Factorial)

                elif(choice_Operation == 11):
                    Inc = x+1
                    print("Increment of ",x,"=",Inc)

                elif(choice_Operation == 12):    
                    Dec = x-1
                    print("Decrement of ",x,"=",Dec)

            elif(choice_Operation == 13):
                print('''
 Exiting From Calculator...
 Returning To Main Menu...  
                ''')
                break;

            else:
                print("Invalid Number Choosen")

            print()

            Ask_Exit=input("Do You Want To Exit From Calculator Y/N : ")

            if(Ask_Exit=='y'):
                print('''
 Exiting From Calculator...
 Returning To Main Menu...  
              ''')
                break;
            else:
                continue;
    
    elif i==2:

        while True:
            print('''
            
 Unit Conversion
                  
 1.Hours To Second
 2.Sec To Hours
 3.Exit
                  ''')
            C_C=int(input("Your Choice : "))

            if C_C==1:
                print("Hour To Second")
                Hours=int(input("Enter Hours : "))
                Sec=Hours*60*60
                print(Sec,"Sec")

            elif C_C==2:
                print("Seconds To Hours")
                Sec=int(input("Enter Seconds : "))
                Hours=Sec/3600
                print(Hours,"Hours")

            elif C_C==3:
                print('''
 Exiting From Unit Conversion...
                      ''')
                break;
    
    elif i==3:
        print('''
 Closing Operations...
 Singing Off....
 Thank You For Using Calculator :)
              ''')
        break;
    else:
        print("Invalid Input")