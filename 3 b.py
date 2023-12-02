#!/usr/bin/env python
# coding: utf-8

# In[ ]:


list=[]
square=[]
for i in range (0,5):
    n=int(input ("Enter numbers:"))
    list.append(n)
print("Entered list are:",list)
square=[(i*i) for i in list]
print("Square of the list are:",square)

