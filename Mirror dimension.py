#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python program that accepts a word from the user and reverse it.

word=input("enter the word")
reverse_word= ""
index=len(word)-1
while index >=0:
    reverse_word=reverse_word+word[index]
    index=index-1
print("the reverseword is :",reverse_word)


# In[ ]:




