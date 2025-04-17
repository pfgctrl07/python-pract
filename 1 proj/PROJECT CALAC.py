#MINI CALCULATOR

#addition
def add(a,b):
    c=a+b
    return c

#subtraction
def sub(a,b):
    c=b-a
    return c

#division
def div(a,b):
    c=a/b
    return c

#floor division
def fd(a,b):
    c=a//b
    return c
        
#remainder
def mod(a,b):
    c=a%b
    return c

#multiplication
def mul(a,b):
    c=a*b
    return c

#exponent
def exp(a,b):
    c=a**b
    return c

#square
def sqt(a):
    c=a**2
    return c

#root
def root(a):
    c=a**0.5
    return c
    
print("****** WELCOME TO MINI CALCULATOR *******")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.DIVISION")
print("4.FLOOR DIVISION")
print("5.MODULO")
print("6.MULTIPLICATION")
print("7.EXPONENTATION")
print("8.SQUARE")
print("9.ROOT")
vx=1
while(vx==1):
    ch=int(input("ENTER THE CHOICE OF OPERATION NEED TO BE DONE "))

    if(ch==1):
           num1=int(input("enter the first number "))
           num2=int(input("enter the second number "))
           
           re=add(num1,num2)
           print("THE ANSWER IS ",re)

    if(ch==2):
           num1=int(input("enter the first number "))         
           num2=int(input("enter the second number "))
           re=sub(num1,num2)
           print("THE ANSWER IS ",re)

    if (ch==3):
           num1=int(input("enter the first number "))
           num2=int(input("enter the second number "))
           re=div(num1,num2)
           print("THE ANSWER IS ",re)

    if(ch==4):
           num1=int(input("enter the first number "))         
           num2=int(input("enter the second number "))
           re=fd(num1,num2)
           print("THE ANSWER IS ",re)         

    if(ch==5):
           num1=int(input("enter the first number "))
           num2=int(input("enter the second number "))
           re=mod(num1,num2)
           print("THE ANSWER IS ",re)         

    if(ch==6):
           num1=int(input("enter the first number "))
           num2=int(input("enter the second number "))
           re=mul(num1,num2)
           print("THE ANSWER IS ",re) 

    if(ch==7):
           num1=int(input("enter base number: "))
           num2=int(input("enter power number: "))
           re=exp(num1,num2)
           print("THE ANSWER IS ",re)         

    if(ch==8):
           num=int(input("enter the number"))
           re=sqt(num)
           print("THE ANSWER IS ",re)        

    if(ch==9):
           num=int(input("enter the number"))
           re=root(num)
           print("THE ANSWER IS ",re)
    if(ch>=10)or(ch<1):
           print("invalid")
    else:
        vx=int(input("do you want to continue if want enter 1 if not enter 0 : "))
        
                   

                
                    
        

