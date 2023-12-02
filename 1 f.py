#!/usr/bin/env python
# coding: utf-8

# In[ ]:


list=[2,5,6,7,8,9]
print(list)
for i in list:
    if i%2==0:
        list.remove(i)
print("Display the numbers after removing even numbers")
print(list)

