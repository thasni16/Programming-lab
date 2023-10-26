#!/usr/bin/env python
# coding: utf-8

# In[10]:


current=int(input("Enter current year:"))
final=int(input("Enter the final year:"))
leap=[]
for i in range(current,final+1):
    if(i%4==0 and i%100!=0)or(i%400==0):
        leap.append(i)
print("Leap year",leap)
    
    


# In[ ]:





# In[ ]:




