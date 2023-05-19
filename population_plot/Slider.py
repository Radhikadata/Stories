#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


# In[2]:


import os


# In[3]:


DATA_FOLDER = os.getcwd()


# In[4]:


print(DATA_FOLDER)


# In[5]:


get_ipython().run_line_magic('cd', '/Users/radhika/Downloads/Radhika-maps/Stories')


# In[6]:


DATA_FOLDER = os.getcwd()


# In[7]:


print(DATA_FOLDER)


# In[8]:


PREPROCESS_FOLDER  = f"{DATA_FOLDER}/population_plot"
OUTPUT_FOLDER = f"{DATA_FOLDER}/output"
DF_CSV = f"{PREPROCESS_FOLDER}/Data_2095.csv"
Splot_HTML_OUTPUT = f'{OUTPUT_FOLDER}/tfrvsbirth_index.html'


# In[9]:


df = pd.read_csv(DF_CSV)


# In[10]:


df.head()


# In[11]:


type(df['Pop'])


# In[12]:


df = df.rename(columns={'BR':'Birth Rate','TFR':'Total Fertility Rate'})


# In[13]:


df['Pop']= df['Pop'].astype(int)
df['Birth']=df['Birth'].astype(int)


# In[14]:


df['Pop in Million']=df['Pop']/1000000
df['Birth per Thousand']=df['Birth']/1000


# In[15]:


df.head()


# In[16]:


fig= px.scatter(df,x= "Total Fertility Rate", y= "Birth per Thousand", animation_frame="Year", animation_group="State",size="Pop in Million",color="State",
         hover_data={'Birth per Thousand' :True,'State' :True, 'Pop in Million' :True,'Total Fertility Rate' :True},
                log_x=False, size_max=90, title='Birth vs TFR'
        )
    
fig.update_layout(yaxis_title="Birth per Thousand", plot_bgcolor='black',paper_bgcolor='black')
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
fig.update_layout(width=1000, height=800)
fig.update_layout(
    font=dict(
        color='white' 
    )
)

 
fig.write_html(Splot_HTML_OUTPUT)

fig


# In[ ]:




