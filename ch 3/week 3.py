#FUNCTIONS AND RECURSION

#PROBLEM 1

#Create a function add(a, b) that returns the sum of two numbers.

"""

def add(a,b):
    sum=a+b
    return sum

num1=int(input("enter a number"))
num2=int(input("enter anumber"))
ans=add(num1,num2)
print(ans)

"""

#PROBLEM 2

#Define a function square(n) that returns the square of a given number.

"""

def square(n):
    sq=n**2
    return sq

num=int(input("enter the number need to be squared"))
ans=square(num)
print(ans)

"""

#PROBLEM 3

"""

#Write a function that takes a string as input and returns its length.

def il(a):
    ln=len(a)
    return ln

st=input("enter a string ")
ans=il(st)
print(ans)

"""

#PROBLEM 4

#Create a function that takes a list of numbers as input and returns the maximum value.

"""

def maxm(h):
    f=max(h)
    return f
        
num=[]
n=int(input("enter number elements in the list"))
for i in range(n):
    m=int(input("enter the element:"))
    num.append(m)
ans=maxm(num)
print(ans)

"""

#PROBLEM 5

#Write a function count_vowels(s) that returns the number of vowels in a given string.

"""

def vc(f):
    vo="aeiouAEIOU"
    vs=0
    for char in f:
        if char in vo:
            vs+=1

    return vs
st=input("enter the string ")
ans=vc(st)
print(ans)

"""
#PROBLEM 6

#Implement a function to compute the greatest common divisor (GCD) of two numbers using recursion.

"""

def gcd(a, b):
    if b == 0:
        return a  
    return (gcd(b, a % b))


num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
ans=gcd(num1,num2)
print(ans)

"""

#PROBLEM 7

#Implement a recursive function to reverse a given string.

"""

def rs(s):
    if(len(s)==0):
        return s
    return rs(s[1:])+s[0]

st=input("enter a string")
a=rs(st)
print(a)

"""



            
    

