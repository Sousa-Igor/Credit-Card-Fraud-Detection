#%%
import pandas as pd
import sqlite3

# %%
df = pd.read_csv('credit_card_fraud_2026.csv')
df.head()

con = sqlite3.connect('database.db')

df.to_sql('credit',
          con,
          if_exists='replace',
          index=False)
# %%
