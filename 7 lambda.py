#!/usr/bin/env python
# coding: utf-8

# In[1]:


sqarea=lambda s:s*s
rectarea=lambda l,b:l*b
triarea=lambda h,ba:(1/2)*h*ba
s=int(input("Enter the side of length of square:"))
l=int(input("Enter the  length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
h=int(input("Enter the height of triangle:"))
ba=int(input("Enter the base of triangle:"))
print("area of square:",sqarea(s))
print("area of rectangle:",rectarea(l,b))
print("area of triangle:",triarea(h,ba))




# In[ ]:




