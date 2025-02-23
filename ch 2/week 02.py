# CONDITIONAL STATEMENTS

#PROBLEM 1

#Age Group Checker
    #Problem: Write a program that takes an age as input and outputs the corresponding age group:

    #Age < 13: "Child"
    #13 ≤ Age < 20: "Teenager"
    #20 ≤ Age < 60: "Adult"
    #Age ≥ 60: "Senior Citizen"

"""age=int(input("enter the age:"))
if(age>0):
    if(age<13 ):
        print("child")
    elif(age>=13 and age<20):
        print("teenager")
    elif(age>=20 and age<60):
        print("adult")
    elif(age>=60):
        print("senior citizen")
else:
    print("invlaid entry")"""

#PROBLEM 2

#Grading System
    #Problem: Write a program that takes a percentage score as input and prints the grade:

    #90% and above: "A"
    #80%–89%: "B"
    #70%–79%: "C"
    #60%–69%: "D"
    #Below 60%: "F"

    
"""per=int(input("enter the percentage:"))
if(per>0):
    if(per<60):
        print("F")
    elif(per>=60 and per<=69):
        print("D")
    elif(per>=70 and per<=79):
        print("C")
    elif(per>=80 and per<=89):
        print("B")
    elif(per>=90):
        print("A")
else:
    print("invald entry")"""

#PROBLEM 3

#Print Multiplication Table
    #Take an integer input and print its multiplication table up to 10 using a loop.

"""x=int(input("enter thr number:"))

for i in range (1,11):

    print(x, "*" ,i,"=", x*i)"""

#PROBLEM 4

#Pattern Printing
   #Print the following pattern for n = 5:
    #*
    #**
    #***
    #****
    #*****

"""n=int(input("enter how many times need to be printed:"))

for i in range(1,n+1):
    print("*"*i)"""

#PROBLEM 5

#Write a program to check if a character entered by the user is a vowel or consonant.

"""a=input("enter a charecter")
if(a=='a'or a=='e' or a=='i' or a=='o' or a=='u' or a=='A' or a=='E' or a=='I' or a=='O' or a=='U'):
    print("it is a vowel")
else:
    print("it is not a vowel")"""

#PROBLEM 6

#Write a program to find the largest among three numbers entered by the user.

"""n1=int(input("enter 1st number:"))
n2=int(input("enter 2nd number:"))
n3=int(input("enter 3rd number:"))
if(n1>n2 and n1>n3):
    print("largest is",n1)
elif(n2>n1 and n2>n3):
    print("largest is",n2)
else :
    print("largest is",n3)"""

#PROBLEM 7
    
#Write a Python program to check if a number is an Armstrong number. A number is an Armstrong number if the sum of its own digits each raised to the power of the number of digits is equal to the number itself.

    #Input: 153 → Output: Armstrong Number
    #Input: 9474 → Output: Armstrong Number


"""num=int(input("enter a number:"))
ns=str(num)
c=len(ns)
p=0

for digit in ns:
    p+=int(digit)**c

if p==num:
    print("yes it is an armstrong number")

else:
    print("no it is not an armstrong number")"""
