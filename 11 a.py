#!/usr/bin/env python
# coding: utf-8

# In[1]:


f=open("file.txt","r")
content=f.readlines()
c=[i.strip() for i in content]
print(c)
f.close()


# In[ ]:




