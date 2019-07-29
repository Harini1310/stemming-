#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer


# In[39]:


file=open(r"C:\Users\Harini\Downloads\tweets.csv")
my_lines_list=file.readlines()
my_lines_list


# In[43]:


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
porter=PorterStemmer()

def stemSentence(sentence):
    token_words=word_tokenize(sentence)
    token_words
    stem_sentence=[]
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)


print("Stemmed sentence")
for i in my_lines_list:
    x=stemSentence(i)
    print(x)


# In[54]:


stem_file=open(r"C:\Users\Harini\Desktop\tweets.txt",mode="a+",encoding="utf-8")
for line in my_lines_list:
    stem_sentence=stemSentence(line)
    stem_file.write(stem_sentence)

stem_file.close()


# In[ ]:




