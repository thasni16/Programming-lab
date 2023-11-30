#!/usr/bin/env python
# coding: utf-8

# In[4]:


n=int(input("Enter the number of rows:"))
for i in range(0,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(0,i-1):
        print("*",end=" ")
    print()


# In[ ]:




