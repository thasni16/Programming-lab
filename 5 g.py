#!/usr/bin/env python
# coding: utf-8

# In[3]:


def modify(string):
    if string.endswith("ing"):
        newstr=string+"ly"
    else:
        newstr=string+"ing"
    return newstr
n=input("Enter a string:")
result=modify(n)
print("The new string is:",result)


# In[ ]:




