#!/usr/bin/env python
# coding: utf-8

# In[ ]:



dict1={} 
for i in range(0,4):
    key=(input("Enter a key:"))
    value=input("Enter a value:")
    dict1[key]=value
print("Dictionary in ascending order:",dict(sorted(dict1.items())))
print("Dictionary in decending order:",dict(sorted(dict1.items(),reverse=True)))

