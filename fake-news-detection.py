#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


# In[18]:


df=pd.read_csv('news.csv')
df.shape
df.head()


# In[19]:


labels=df.label
labels.head()


# In[20]:


x_train,x_test,y_train,y_test=train_test_split(df['text'], labels,test_size=0.2,random_state=7)


# In[21]:


tfidf_vectorizer=TfidfVectorizer(stop_words='english',max_df=0.7)
tfidf_train=tfidf_vectorizer.fit_transform(x_train)
tfidf_test=tfidf_vectorizer.transform(x_test)


# In[22]:


pac=PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train,y_train)
y_pred=pac.predict(tfidf_test)
score=accuracy_score(y_test,y_pred)
print(f'Acuracy:{round(score*100,2)}%')


# In[23]:


confusion_matrix(y_test,y_pred,labels=['FAKE','REAL'])


# In[ ]:




