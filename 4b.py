#!/usr/bin/env python
# coding: utf-8

# In[ ]:


str=(input("Enter a string:"))
new=str[0]+str[1:].replace(str[0],'$')
print("The new string is:",new)

