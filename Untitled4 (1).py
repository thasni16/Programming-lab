#!/usr/bin/env python
# coding: utf-8

# In[17]:


def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
g=gcd(n1,n2)
print("gcd(num1,num2):",g)




    
    


# In[22]:


list=[2,5,6,7,8,9]
print(list)
for i in list:
    if i%2==0:
        list.remove(i)
print("Display the numbers after removing even numbers")
print(list)







