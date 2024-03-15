#!/usr/bin/env python
# coding: utf-8

# # This Netflix dataset has information of TV shows and movies available on Netflix till March 2021
# 
# # This dataset is imported from Flixable and available free of cost on Kaggle
# 
# # ![netflix.webp](attachment:netflix.webp)

# In[1]:


#Importing the dataset
import pandas as pd
data= pd.read_csv(r"C:\Users\DEEL\Downloads\file.csv")


# In[3]:


data


# # Getting some information about dataset

# # 1.) head()

# In[4]:


data.head()       #to show top 5 records of dataset 


# # 2.) tail()

# In[5]:


data.tail()  #to show bottom 5 records of dataset 


# # 3.)shape

# In[7]:


data.shape      #to find number of rows and columns 


# # 4.) size

# In[8]:


data.size   #to show total number of elements in the dataset 


# # 5.) columns 

# In[9]:


data.columns      #to show all the columns of the dataset 


# # 6.) datatypes 

# In[10]:


data.dtypes    #to show datatypes of columns 


# # 7.) information

# In[11]:


data.info()     #to show indexes,coluns,data-types of each column,memory at once 


# # Task-1 : Is there any duplicate record? If yes then remove it

# # duplicate()

# In[12]:


data.head()


# In[13]:


data.shape


# In[16]:


data[data.duplicated()]                        # to check row wise for duplicates


# In[18]:


data.drop_duplicates(inplace=True)                        #to remove duplicate ros permanently


# In[19]:


data[data.duplicated()]


# In[20]:


data.shape


# # Task-2 Is there any NULL value present in any column ? Show wth heat map

# # isnull()

# In[21]:


data.head()


# In[22]:


data.isnull()


# In[23]:


data.isnull().sum()


# # seaborn library (heat map)

# In[26]:


import seaborn as  sns          # to import seaborn library 


# In[27]:


sns.heatmap(data.isnull())     # to plot the heatmap to show null values 


# # Q.1. For the show of  'House Of Cards',  what is show id and who is the director of the show ?

# # isin()

# In[29]:


data.head()


# In[30]:


data[data['Title'].isin(['House of Cards'])]     # to show all records of a particuar item in  dataset 


# # Q.2. In which year highest movies and shows were made ? Show with the help of bar graph

# # dtypes

# In[32]:


data.dtypes


# # to_datetime

# In[33]:


data['Date_N']=pd.to_datetime(data['Release_Date'])


# In[35]:


data.head()


# In[36]:


data.dtypes


# # dt.year.value_counts()

# In[37]:


data['Date_N'].dt.year.value_counts()  # it counts occurences of al individual years in date columns 


# # Bar Graph

# In[38]:


data['Date_N'].dt.year.value_counts().plot(kind='bar')


# # Q.3. How many movie and TV shows are in the dataset? 

# # groupby()

# In[39]:


data.head(2)


# In[40]:


data.groupby('Category').Category.count()   #to group all unique items of a column and show their count 


# # Q.4. Show all the movies tht were released in the year 2000

# # Creating new column

# In[42]:


data.head(2)


# In[43]:


data['Year']=data['Date_N'].dt.year     #to create a new year column which will consider only year 


# In[44]:


data.head(2)


# # Filtering

# In[46]:


data[(data['Category']=='Movie')&(data['Year']==2020)]


# # Q.5. Show only the titles of all TV shows that were released in India 

# # Filtering

# In[47]:


data.head(2)


# In[49]:


data[(data['Category']=='TV Show')&(data['Country']=='India')]['Title']


# # Q.6. Show top 10 directors who gave highest number of TV shows and movies to Netflix

# # value_counts()

# In[50]:


data.head(2)


# In[52]:


data['Director'].value_counts().head(10)


# # Q.7. Show all the records where category is movie and type is comedy or country is UK

# # Filtering ( AND ,OR operators)

# In[53]:


data.head(2)


# In[54]:


data[(data['Category']=='Movie')&(data['Type']=='Comedies')]


# In[55]:


data[(data['Category']=='Movie')&(data['Type']=='Comedies')| (data['Country']=='United Kingdom')]


# # Q.8. In how many movies/shows Tom Cruise was cast?

# In[57]:


data.head(2)


# # filtering 

# In[58]:


data[data['Cast']=='Tom Cruise']


# # Creating new dataframe 

# In[59]:


data_new=data.dropna()


# In[60]:


data_new.head(2)


# In[61]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]


# # Q.9. What are different ratings defined by Netflix?
# 

# # nunique()

# In[62]:


data.head(2)


# # nunique()

# In[63]:


data['Rating'].nunique()


# # unique()

# In[64]:


data['Rating'].unique()


# # Q9.1 How many movies got 'TV-14' rating in Canada?

# In[65]:


data.head(2)


# In[67]:


data[(data['Category']=='Movie')&(data['Rating']=='TV-14')].shape


# In[68]:


data[(data['Category']=='Movie')&(data['Type']=='Comedies')&(data['Country']=='Canada')]


# # Q9.2 How many TV show got R rating after 2018?

# In[69]:


data.head(2)


# In[70]:


data[(data['Category']=='TV Show')&(data['Rating']=='R')]


# In[71]:


data[(data['Category']=='TV Show')&(data['Rating']=='R')&(data['Year']>2018)]


# # Q.10. What is the maximum duration of TV show / Movie on Netflix?

# In[72]:


data.head(2)


# In[73]:


data.Duration.unique()


# In[74]:


data.Duration.dtypes


# # str.split()

# In[75]:


data.head(2)


# In[77]:


data[['Minutes','Unit']]=data['Duration'].str.split(' ',expand=True)


# In[78]:


data.head(2)


# In[79]:


data['Minutes'].max()


# In[80]:


data['Minutes'].min()


# In[81]:


data['Minutes'].mean()


# In[82]:


data.dtypes


# # Q.11. How can we sort dataset by year?

# In[83]:


data.head(2)


# In[84]:


data.sort_values(by='Year')


# In[86]:


data.sort_values(by='Year',ascending=False).head(10)


# In[ ]:




