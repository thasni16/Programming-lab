#!/usr/bin/env python
# coding: utf-8

# In[15]:


def factorial(n):
    fact=1
    if n<0:
        print("Invalid input")
        return
    elif n==0:
        return 1
    else:
        for i in range(1,n+1):
            fact=fact*i
        return fact
num=int(input("Enter a number to find factorial:"))
result=factorial(num)
print("The factorial of given number:",result)


# In[7]:


def fibonacci(n):
    a=0
    b=1
    if n==0:
        return a
    elif n==1:
        return b
    else:
        print(a)
        print(b)
        for i in range(2,n):
            fib=a+b
            a=b
            b=fib
            print(fib)
num=int(input("Enter a number:"))
print("The fibonacci series for given number",num,"is:")
fibonacci(num)


# In[9]:


list=[]
total=0
for i in range(4):
    n=int(input("Enter a number:"))
    list.append(n)
print(list)
for i in list:
    total=total+i
print("sum of all items in the list:",total)




# In[12]:


def pyramid(row):
    for i in range(1,row+1):
        for j in range(1,i+1):
            print(i*j,end=" ")
        print("\n")
n=int(input("Enter a number:"))
pyramid(n)


# In[24]:


square=[]
initial=int(input("Enter initial number"))
final=int(input("Enter final number"))
for i in range(initial,final+1):
    sqr=i*i
    d=sqr
    while (d>0):
        digit=d%10
        if digit%2==0:
            d//=10
            if d==0:
                square.append(sqr)
        else:
            break
print(square)



# In[ ]:




