# DATATYPES

#PROBLEM 1

# Write a program to determine if a given number is even or odd.

"""a=int(input("enter a number:"))
if(a==0):
    print("neither even or odd")
elif(a%2==0):
    print("even")
else:
    print("odd")"""

#PROBLEM 2

# How can you convert a number to a string in Python? Write an example

"""a=int(input("enter a number:"))
print(a,"is a",type(a))
b=str(a)
print(b,"is a",type(b))"""

# STRING

# PROBLEM 1

# Write a program to concatenate two strings entered by the user.

"""a=input("enter a string 1 :")
b=input("enter a string 2 :")
c=a+" "+ b
print(c)"""

# PROBLEM 2

# Write a program to count the number of vowels in a string.

"""count=0
a=input("enter a string")
vowels="aeiouAEIOU"
for i in a:
    if i in vowels:
        count+=1

print(count)"""

#PROBLEM 3

#Create a program to remove all spaces from a given string

"""a=input("enter a string ")
b=""
for i in a:
    if (i !=" "):
        b+=i
print (b)"""

# LISTS

#PROBLEM 1

#Write a program to remove a element from a list.

"""a=[]
n=int(input("enter the length of the list:"))
for i in range(n):
    val=int(input("enter the value:"))
    a.append(val)
print(a)
r=int(input("enter the element need to eliminated:"))
if(r in a):
    a.remove(r)
    print(a)
    
else:
    print("no such element")"""

#PROBLEM 2

#write a program to return a list containing values of orginal list multiples of 5

"""a=[]
b=[]
n=int(input("enter length of the list:"))
for i in range(n):
    val=int(input("enter the value:"))
    a.append(val)
for i in range(n):
    if(a[i]%5==0):
        b.append(a[i])
print(b)"""

# TUPLES

#PROBLEM 1

#Given a tuple of numbers, write a program to find the largest and smallest number in the tuple.

"""a=[]
n=int(input("enter the no of elemnts"))
for i in range (n):
    el=int(input("enter the values"))
    a.append(el)
t=tuple(a)
largest=max(t)
smallest=min(t)
print(f"largest {largest}")
print(f"smallest {smallest}")"""

#PROBLEM 2

#write a program to find index value of a specific element

"""a=[]
n=int(input("enter the no of elemnts"))
for i in range (n):
    el=int(input("enter the values"))
    a.append(el)
t=tuple(a)
v=int(input("enter the nummber need to be searched :"))
if(v in t):
        i=t.index(v)
        print(f"index is {i}")
else:
    print("no such element exists")"""

# SETS

#PROBLEM 1

#Create a set from a list, then remove an element from the set without causing an error if the element doesn’t exist.

"""a=[]
n=int(input("enter the no of elemnts"))
for i in range (n):
    el=int(input("enter the values"))
    a.append(el)
s=set(a)
el=int(input("enter elemt need to be eliminated:"))
if el in s:
    s.remove(el)
    print(f"modified set {s}")
else:
    print("no such element exists:")"""

#PROBLEM 2

#Given two sets of student names, find the names that are common to both classes.

"""a=[]
n=int(input("enter the no of elemnts"))
for i in range (n):
    el=input("enter the values")
    a.append(el)
s1=set(a)
b=[]
n1=int(input("enter the no of elemnts"))
for i in range (n1):
    hl=input("enter the values")
    b.append(hl)
s2=set(b)

print(s1 & s2)"""

#PROBLEM SOLVING QUESTON

#Write a program to:

    #Take a list of numbers from the user.
    #Use a set to find all prime numbers in the list.
    #Store these prime numbers in a tuple and print them

"""numb=[]
n=int(input("enter number of elements:"))
for i in range(n):
    val=int(input("enter a number:"))
    numb.append(val)
prime=set()
for num in numb:
    if num > 1:  
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:  
            prime.add(num)
primet = tuple(prime)
print("Prime numbers in the list:", primet)"""




        
