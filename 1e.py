#!/usr/bin/env python
# coding: utf-8

# In[6]:


list1=[1,2,7,9,4]
list2=[5,3,8,7,1]
a=len(list1)
b=len(list2)
if a==b:
    print("The two lists are of same length")
else:
    print("Not same length")
c=sum(list1)
d=sum(list2)
if c==d:
    print("Sum of lists is same")
else:
    print("Sum of list is not same")
for i in list1:
    if i in list2:
        print(" elements occur in both are",i)
    



# In[ ]:


