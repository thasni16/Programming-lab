#!/usr/bin/env python
# coding: utf-8

# In[4]:


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>b and a>c:
    print(a ,"is the biggest number")
elif b>c:
    print(b ,"is the biggest number")
else:
    print(c ,"is the biggest number")



