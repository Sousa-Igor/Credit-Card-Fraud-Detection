#%%
import pandas as pd
import sqlalchemy
from tqdm import tqdm
# %%

def ingest_table(tabela):
    for i in tqdm(tabela):
        with open(f"F:/igor/Python/Credit Card Fraud Detection/src/engineering/{i}.sql", 'r') as open_file:
            query = open_file.read()

        df = pd.read_sql(query, origin_engine)

        df.to_sql(f"{i}", target_engine, index=False)

#%%
origin_engine = sqlalchemy.create_engine("sqlite:///../../data/database.db")
target_engine = sqlalchemy.create_engine("sqlite:///../../data/fraud.db")

tabelas = ["fs_customer","fs_merchant","fs_security","fs_temporais","fs_transaction"]

ingest_table(tabelas)
