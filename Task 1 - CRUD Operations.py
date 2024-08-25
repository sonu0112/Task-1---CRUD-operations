#!/usr/bin/env python
# coding: utf-8

# # TASK 1 - CRUD Operations On Fifa WorldCup Dataset.

# In[ ]:





# In[33]:


#import libraries
import pandas as pd


# In[34]:


#read csv file using pandas
data = pd.read_csv(r"C:\Users\suyas\Downloads\WorldCups.csv")


# In[35]:


#initial dataframe
df = pd.DataFrame(data)


# In[41]:


#top 20 rows
df.head(20)


# In[ ]:





# #### CREATE: Insert New Records Into The Dataset.

# In[38]:


#adding new record
new_record = pd.DataFrame({
    'Year':[2018],
    'Country':['spain'],
    'Winner':['India'],
    'Runners-Up':['France'],
    'GoalsScored':[150.0],
    'MatchesPlayed':[66]  
    })
df = pd.concat([df,new_record], ignore_index=True)
print(df)


# In[39]:


df.head(21)


# In[ ]:





# #### READ: Retrieve And Display Specific Records From The Dataset

# In[ ]:





# In[43]:


#retrieve specific records where 'GoalsScored' is greater than 150
specific_records = df[df['GoalsScored']>150]

#diplay the records
print(specific_records)


# In[ ]:





# #### UPDATE : Modify Existing Records In The Dataset

# In[ ]:





# In[50]:


#Modify a specific record by index
df.at[1,'Country'] = 'India'

#save the update dataset
df.to_csv(r"C:\Users\suyas\Downloads\WorldCups.csv", index=False)


# In[51]:


df.head(8)


# In[ ]:





# #### DELETE : Remove Specific Records From The Dataset

# In[52]:


#remove a specific records by index
df = df.drop(index=6)


# In[53]:


df.head(9)


# In[ ]:




