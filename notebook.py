#!/usr/bin/env python
# coding: utf-8

# In[388]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


# In[389]:


prompts_train = pd.read_csv(r"C:\Users\rachitgandhi1\Downloads\commonlit-evaluate-student-summaries\prompts_train.csv")
prompts_test = pd.read_csv(r"C:\Users\rachitgandhi1\Downloads\commonlit-evaluate-student-summaries\prompts_test.csv")

summaries_train = pd.read_csv(r"C:\Users\rachitgandhi1\Downloads\commonlit-evaluate-student-summaries\summaries_train.csv")
summaries_test = pd.read_csv(r"C:\Users\rachitgandhi1\Downloads\commonlit-evaluate-student-summaries\summaries_test.csv")

sample_submission = pd.read_csv(r"C:\Users\rachitgandhi1\Downloads\commonlit-evaluate-student-summaries\sample_submission.csv")



# In[390]:


prompts_train


# In[391]:


train = summaries_train.merge(prompts_train, how="left", on="prompt_id")
test = summaries_test.merge(prompts_test, how="left", on="prompt_id")

train


# In[392]:


train["prompt_id"] = train["prompt_id"].astype("category")
test["prompt_id"] = test["prompt_id"].astype("category")


# In[393]:


order_prompt_ids = train['prompt_id'].values.tolist()
order_prompt_id_set = set(order_prompt_ids)
order_prompt_id_set


# In[394]:


train = train.sort_values(by=['prompt_id'])
test = test.sort_values(by=['prompt_id'])


# In[395]:


import matplotlib.pyplot as plt
student_ids = train['student_id'].values.tolist()
student_id_set = set(student_ids)
print(len(student_id_set))
#means each student is unique


# In[396]:


train.drop('prompt_title', axis=1, inplace=True)
train.drop('prompt_question', axis=1, inplace=True)
train.drop('prompt_text',axis=1, inplace=True)
train


# In[397]:


test.drop('prompt_title', axis=1, inplace=True)
test.drop('prompt_question', axis=1, inplace=True)
test.drop('prompt_text',axis=1, inplace=True)
test


# In[398]:


def content_plotter(df):
    # create a figure and axis object
    fig, ax = plt.subplots()

    # plot each column in different colors against the 'tudent_id' column
    
    #ax.scatter(df['student_id'], df['wording'], color='purple', label='Wording Score')
    #ax.scatter(df['student_id'], df['content'], color='green', label='Content Score')

    ax.scatter(df['student_id'], df['content']-df['wording'], color='green', label='Content - Wording')


    # add labels and title to the plot
    ax.set_xlabel('Student ID')
    ax.set_ylabel('Value')

    # add a legend to the plot
    ax.legend()

    # show the plot
    plt.show()
    

train['prompt_id'].value_counts()
train1 = train.iloc[:2057]
train2 = train.iloc[2057:4066]
train3 = train.iloc[4066:6062]
train4 = train.iloc[6062:7165]
train1


# In[399]:


content_plotter(train1)



# In[400]:


content_plotter(train2)


# In[401]:


content_plotter(train3)


# In[402]:


content_plotter(train4)

