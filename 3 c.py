#!/usr/bin/env python
# coding: utf-8

# In[ ]:


vowels=['a','e','i','o','u','A','E','I','O','U']
vowel=[]
word=input("Enter an word:")
vowel=[i for i in word if i in vowels]
print(vowel)

