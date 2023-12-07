#!/usr/bin/env python
# coding: utf-8

# In[ ]:


dict={}
for i in range(0,3):
    key=int(input("enter a key:"))
    value=(input("enter a value:"))
    dict[key]=value
print("first dictionary",dict)
dict1={}
for i in range(0,3):
    key=int(input("enter a key:"))
    value=(input("enter a value:"))
    dict1[key]=value
print("second dictionary",dict1)
dict.update(dict1)
print("merged dictionary",dict)

