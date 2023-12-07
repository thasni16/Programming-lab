#!/usr/bin/env python
# coding: utf-8

# In[ ]:


first=[]
count=0
for i in range(0,3):
    ele=(input("Enter the names:"))
    first.append(ele)
print(first)
for i in first:
    count+=i.count('a')
print("The number of occurance 'a' in list:",count)

