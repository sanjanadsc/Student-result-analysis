#!/usr/bin/env python
# coding: utf-8

# # 1.Import Iibraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # 2.Import data

# In[19]:


df = pd.read_csv('students_data.csv')
df


# # 3.Data information

# In[20]:


print(df.head())


# In[21]:


df.info()


# In[22]:


df.describe()


# In[23]:


df.isnull().sum()


# # 4.Data transformation

# In[24]:


#drop unnamed column
df = df.drop("Unnamed: 0", axis= 1)


# In[25]:


df


# # 5. Analysis using charts

# In[30]:


#gender distribution
plt.figure(figsize= (5,5))
ax=sns.countplot(data=df, x='Gender')
ax.bar_label(ax.containers[0])
plt.show()


# In[31]:


#We analysed that female is more than boys


# In[34]:


#effect on student academics of parents eduction
gb=df.groupby('ParentEduc').agg({'MathScore':"mean", "ReadingScore":"mean","WritingScore":"mean"})
print(gb)


# In[37]:


sns.heatmap(gb, annot= True)
plt.figure(figsize= (5,5))
plt.show()


# In[38]:


#We have concluded that education of parents effected the students academics


# In[39]:


#effect on student academics of parents marital status
gb1=df.groupby('ParentMaritalStatus').agg({'MathScore':"mean", "ReadingScore":"mean","WritingScore":"mean"})
print(gb1)


# In[40]:


sns.heatmap(gb1, annot= True)
plt.figure(figsize= (5,5))
plt.show()


# In[41]:


#We have concluded that there is no/negligible impact on the students score due to parents's marital status


# In[42]:


#Outlier detection
sns.boxplot(data= df, x='MathScore')
plt.show()


# In[54]:


#Distribution of ethnic groups
groupA= df.loc[(df['EthnicGroup']=='group A')].count()
groupB= df.loc[(df['EthnicGroup']=='group B')].count()
groupC= df.loc[(df['EthnicGroup']=='group C')].count()
groupD= df.loc[(df['EthnicGroup']=='group D')].count()
groupE= df.loc[(df['EthnicGroup']=='group E')].count()

mlist= [groupA["EthnicGroup"], groupB["EthnicGroup"], groupC["EthnicGroup"], groupD["EthnicGroup"], groupE["EthnicGroup"],]
labels = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E']

plt.pie(mlist, labels=labels, autopct='%1.1f%%')
plt.show()


# In[55]:


#We conclude the Group C has highest ethnic distribution


# In[ ]:




