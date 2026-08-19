#%%
import pandas as pd
import sqlalchemy
# %%
data = pd.read_csv("../../data/credit_card_fraud_2026.csv")
engine = sqlalchemy.create_engine("sqlite:///:memory:")
sql_files = ["fs_customer","fs_merchant","fs_security","fs_temporais","fs_transaction"]
data.to_sql("credit", engine, index=False)

#%%
for file in sql_files:
    with open(f"../engineering/{file}.sql", "r") as query_txt:
        query = query_txt.read()

    df_feature = pd.read_sql(query, engine)

    table_name = file.replace(".sql", "")

    df_feature.to_sql(
        table_name,
        engine,
        index=False,
        if_exists="replace"
    )

# %%
with open("../analytics/abt.sql", "r") as file:
    final_query = file.read()
df = pd.read_sql(final_query, engine)

#%%

df = df.drop(columns="is_fraud")
# %%
model_full = pd.read_pickle("../../models/modelo_final.pkl")
model = model_full["modelo"]
# %%
model.predict(df)

