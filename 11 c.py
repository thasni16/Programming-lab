#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
with open("data.csv","r") as files:
    dt=csv.reader(files)
    for r in dt:
        print("".join(r))


# In[ ]:




