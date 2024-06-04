# Author: github.com/owaisahmedkhan725

# Calculator v-1.5
# Calculator++
# This Can Run the program in loops until exit.
# Making the Calculator launch automatically to perform another calculation until exit.

while True:
        
        print ()
        x=int(input("Enter Value 1: "))
        y=int(input("Enter Value 2: "))

        print()

        print ("Choose a number to perform Action")
        print ("For + Press 1")
        print ("For - Press 2")
        print ("For * Press 3")
        print ("For divide Press 4")
        print ("For Square of ",x, "Press 5")
        print ("For Square of ",y, "Press 6")
        print("For",x," Modulus ",y, "Press 7")
        print ("For Increment of ",x, "Press 8")
        print ("For Decrement of ",x, "Press 9")
        print ("For Increment of ",y, "Press 10")
        print ("For Decrement of ",y, "Press 11")
        print ("For Percentage of ",x,"%",y,"Press 12")
        print ()
        print ("Choice action above by Press 1 to 12")
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
        elif(z==5):
            e=x*x
            print("Square of ",x,"=",e)
        elif(z==6):
            f=y*y
            print("Square of ",y,"=",f)
        elif(z==7):
            g=x%y
            print(x,"Modulus",y,"=",g)
        elif(z==8):
            h=x+1
            print("Increment of ",x,"=",h)
        elif(z==9):    
            i=x-1
            print("Decrement of ",x,"=",i)
        elif(z==10):
            j=y+1
            print("Increment of ",y,"=",j)
        elif(z==11):
            k=y-1
            print("Decrement of ",y,"=",k)
        elif(z==12):
            l =(x*y)/100
            print("Percentege of ",x,"%",y,"=",l)
        else:
            print("Invalid Action")
        print()
        
