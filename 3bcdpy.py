#!/usr/bin/env python
# coding: utf-8

# In[4]:


list=[]
square=[]
for i in range (0,5):
    n=int(input ("Enter numbers:"))
    list.append(n)
print("Entered list are:",list)
square=[(i*i) for i in list]
print("Square of the list are:",square)


# In[10]:


vowels=['a','e','i','o','u','A','E','I','O','U']
vowel=[]
word=input("Enter an word:")
vowel=[i for i in word if i in vowels]
print(vowel)
           
           
           


# In[13]:


words=input("Enter an word")
ordinal=[ord(i) for i in words] 
print("ordinal values are:",ordinal)


# In[ ]:




