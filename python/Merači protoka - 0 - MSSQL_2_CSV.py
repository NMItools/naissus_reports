#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, select, engine
import matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

print('Python v' + sys.version)
print('Pandas v' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)


# In[2]:


DB = {
    'drivername': 'mssql+pyodbc',
    'servername': 'VERDI',
    'port': '1433',
    'username': 'nebojsa',
    'password': 'tras659',
    'database': 'SANiN',
    'driver': 'SQL Server Native Client 11.0',
#     'trusted_connection': 'yes',  
#     'legacy_schema_aliasing': 'False'
}

# "mssql+pyodbc://VERDI/SANiN?driver=SQL Server Native Client 11.0;trusted_connection=yes;legacy_schema_aliasing=False"
# "mssql+pyodbc://nebojsa:tras659@VERDI:1433/SANiN?driver=SQL Server Native Client 11.0"

# Create the connection
engine = create_engine(DB['drivername'] + '://' + DB['username'] +':'+ DB['password'] + '@' + DB['servername'] + ':' + DB['port']+ '/' + DB['database'] + '?' + 'driver=' + DB['driver'])
conn = engine.connect()


# In[3]:


# Required for querying tables
metadata = MetaData(conn)


# In[20]:


# # Table to query
# TableName = "SCADA_2020"
# tbl = Table(TableName, metadata, autoload=True, schema="mz")

# # Select all
# sql = tbl.select()

# # run sql code
# result = conn.execute(sql)

# # Insert to a dataframe
# df1 = pd.DataFrame(data=list(result), columns=result.keys())

# # printout
# df1.head()


# In[4]:


# df1 = pd.read_sql_query("[izv].[sp_IZVORISTA_dat_interval] '2019-01-01', '2020-12-01'", engine)
# df2 = pd.read_sql_query("[izv].[sp_IZVORISTA_dat_interval] '2020-01-01', '2020-05-19'", engine)

# df3 = pd.read_sql_query("[dbo].[mp_scada] 'SCADA_2019'", engine)
# df3.head()

df4 = pd.read_sql_query("[dbo].[mp_scada] 'SCADA_2020'", engine)
df4.head()


# In[141]:


# čišćenje naziva kolona od spec karaktera
# df2.columns = df2.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
# df2


# In[5]:


# Export to CSV

# df1.to_csv(TableName+'.csv', index=False)
# print('Done')

TableName = 'SCADA_2020'

df4.to_csv(TableName+'.csv', index=False)
print('Done')

# # Export to EXCEL
# df2.to_excel(TableName+'.xls', sheet_name = 'Izvorišta', index=False)
# print('Done')


# In[6]:


print(df4.columns) 


# In[7]:


print(type(df4.vreme)) 

# # ime kolone sa crticom ili spec karakterom
print(type(df4['I-1-LJB'])) 


# In[8]:


print(type(df4.vreme[0]))
print(type(df4['I-1-LJB'][0]))


# In[185]:


# samo prvi red
# df2.iloc[0]

# samo zadnji red
# df2.iloc[-1]


# In[186]:


# df2.iloc[0]['I-1-LJB']
# # ili
# df2.iloc[0][1]


# In[187]:


# samo vrednosti za 1 kolonu (Ljuberađu npr.)
# df2['I-1-LJB']


# In[188]:


# od reda 0 do reda 144 (jedan dan logova)
# df2[0:144]


# In[9]:


df4.set_index("vreme", inplace=True)
df4


# In[190]:


# df2.loc['2019-01-01 23:50:00']


# In[10]:


# df2.index
# df2['I-1-LJB']

plt.figure(figsize=(50,10))

plt.plot(df4['I-1-LJB'], label='Љуберађа', color='brown')
plt.plot(df4['I-2-DIV'], label='Дивљана', color='red')
plt.plot(df4['I-3-MOK'], label='Мокра', color='purple')
plt.plot(df4['I-4-KR1'], label='Крупац 1', color='orange')
plt.plot(df4['I-4-KR2'], label='Крупац 2', color='yellow')
plt.plot(df4['I-5-STU'], label='Студена', color='cyan')
plt.plot(df4['I-6-MLJ'], label='Миљковац', color='green')
plt.plot(df4['I-7-M10'], label='Медијана 1', color='blue')
plt.plot(df4['I-7-M11'], label='Медијана 11', color='skyblue')
plt.plot(df4['I-7-M2'], label='Медијана 2', color='powderblue')

fig_size = plt.gcf().get_size_inches() #Get current size
sizefactor = 1 #Set a zoom factor
# # Modify the current size by the factor
plt.gcf().set_size_inches(sizefactor * fig_size) 

plt.legend()


# In[11]:


plt.figure(figsize=(50,10))

plt.plot(df4['MRB'], label='МРБ', color='brown')
plt.plot(df4['III-8'], label='Метох', color='red')
plt.plot(df4['M-70-81-17'], label='Рез. Бубањ', color='purple')
# plt.plot(df4['I-4-KR1'], label='Крупац 1', color='orange')
# plt.plot(df4['I-4-KR2'], label='Крупац 2', color='yellow')
# plt.plot(df4['I-5-STU'], label='Студена', color='cyan')
# plt.plot(df4['I-6-MLJ'], label='Миљковац', color='green')
# plt.plot(df4['I-7-M10'], label='Медијана 1', color='blue')
# plt.plot(df4['I-7-M11'], label='Медијана 11', color='skyblue')
# plt.plot(df4['I-7-M2'], label='Медијана 2', color='powderblue')

fig_size = plt.gcf().get_size_inches() #Get current size
sizefactor = 1 #Set a zoom factor
# # Modify the current size by the factor
plt.gcf().set_size_inches(sizefactor * fig_size) 

plt.legend()


# In[12]:


plt.figure(figsize=(50,10))

# plt.plot(df4['I-V-6'], label='Рез. ВИНИК - улаз', color='cyan')
plt.plot(df4['M-20-992-13'], label='Рез. ВИНИК - излаз 1', color='orange')
# plt.plot(df4['M-20-992-27'], label='Рез. ВИНИК - излаз 2', color='yellow')
# plt.plot(df4['M-170-992-34'], label='Рез. ВИНИК - ПС Довод', color='green')
# plt.plot(df4['M-190-21-35'], label='Рез. ВИНИК - ПС Одвод', color='blue')

fig_size = plt.gcf().get_size_inches() #Get current size
sizefactor = 1 #Set a zoom factor
# # Modify the current size by the factor
plt.gcf().set_size_inches(sizefactor * fig_size) 

plt.legend()


# In[13]:


# Close connection
conn.close()


# In[ ]:




