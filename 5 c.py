#!/usr/bin/env python
# coding: utf-8

# In[ ]:


list=[]
total=0
for i in range(4):
    n=int(input("Enter a number:"))
    list.append(n)
print(list)
for i in list:
    total=total+i
print("sum of all items in the list:",total)

