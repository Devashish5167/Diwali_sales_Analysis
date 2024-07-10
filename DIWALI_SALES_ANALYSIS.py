#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import python libraries

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df = pd.read_csv(r'Diwali Sales Data.csv', encoding= 'unicode_escape')


# In[4]:


df.shape


# In[7]:


df.head()


# In[8]:


df.info()


# In[9]:


df.drop(['Status','unnamed1'],axis=1, inplace=True)


# In[11]:


#Check for null values
pd.isnull(df).sum()


# In[12]:


#drop null values
df.dropna(inplace=True)


# In[13]:


df.shape


# In[15]:


#Change data type
df['Amount'] = df['Amount'].astype('int')


# In[16]:


df['Amount'].dtype


# In[17]:


df.columns


# In[18]:


#Rename columne
df.rename(columns={'Marital_Status':'Shaadi'})


# In[20]:


# describe() method returns description of the data in the Dataframe (i.e count, mean,std, etc)
df.describe()


# In[23]:


df[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis

# # Gender

# In[24]:


df.columns


# In[26]:


# plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[32]:


sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)


# ##### From the above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men

# ## Age

# In[35]:


df.columns


# In[39]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[40]:


# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# #### From the above graphs we can see that most of thebuyers are of age group between 26-35yrs female

# ## State

# In[42]:


df.columns


# In[52]:


# Total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data= sales_state, x = 'State', y = 'Orders')


# In[54]:


# Total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data= sales_state, x = 'State', y = 'Amount')


# ##### From the above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively

# ## Marital Status

# In[55]:


df.columns


# In[58]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[62]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# ##### From the above graphs we can see that most of the buyers are married(Women) and they have high purchasing power

# ## Occupation

# In[65]:


sns.set(rc={'figure.figsize':(20,5)})
ax= sns.countplot(data=df, x='Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[66]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# #### From the above graphs we can see that most of the buyers are working in IT, Aviation and Healthcare sector

# ## Product Category

# In[67]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[68]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# #### From the above graphs we can see that most of the sold products are Food,Clothing and Electronics category

# In[69]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# ## Conclusion

# #### Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category

# In[ ]:





# In[ ]:





# In[ ]:




