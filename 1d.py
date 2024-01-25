#!/usr/bin/env python
# coding: utf-8

# In[4]:


list=[]
n=int(input("Enter n:"));
for i in range(n):
    num=int(input("Enter an integer:"));
    if num>100:
        list.append("over")
    else:
        list.append(num)
print(list)



