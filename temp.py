#%%
import pandas as pd
# %%
df = pd.read_csv('data/credit_card_fraud_2026.csv')
df.head()
# %%
df.columns.tolist()
# %%
df['is_new_merchant'].unique()