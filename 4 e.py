#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=input("Enter the string")
w=n.split(" ")
print("The string is:",w)
new=[]
for i in w:
    if i not in new:
        new.append(i)
print(new)
for i in new:
    count=0
    for j in w:
        if i==j:
            count=count+1
    print("The string ",i,"has",count,"times word")   
            

