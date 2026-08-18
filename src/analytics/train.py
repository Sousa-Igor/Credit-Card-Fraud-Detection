#%%
import pandas as pd
import sqlalchemy
import os

from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn import metrics
from sklearn import pipeline
from sklearn import model_selection

from feature_engine import encoding
# %%

engine = sqlalchemy.create_engine("sqlite:///../../data/fraud.db")

with open("F:/igor/Python/Credit Card Fraud Detection/src/analytics/abt.sql", 'r') as open_file:
    query = open_file.read()

df = pd.read_sql(query, engine)
df.head()
# %%

y = df["is_fraud"]
x = df.drop(columns=["is_fraud"])

# %%
X_train, X_test, y_train, y_test = train_test_split(x,y,
                                                    random_state=42)

#%%
print("Taxa de resposta da base Train", y_train.mean())
print("Taxa de resposta da base Test", y_test.mean())
#%%
features = X_train.columns.tolist()
features
# %%
cat_features = X_train.dtypes[X_train.dtypes == "object"].index.tolist()
X_train[cat_features].describe().loc["unique"].sum()
#%%
num_features = list(set(features) - set(cat_features))
num_features
# %%
onehot = encoding.OneHotEncoder(variables=cat_features,
                                drop_last=True)

model = ensemble.RandomForestClassifier(random_state=42)

params = {"min_samples_leaf":[10,25,50,100],
          "n_estimators": [100,200,500,1000],
          "criterion": ['gini', 'entropy'],
          "max_depth": [5,8,10,12,15]}

grid = model_selection.GridSearchCV(model,
                                    param_grid=params,
                                    cv=3,
                                    scoring="roc_auc",
                                    n_jobs=16,
                                    verbose=3)

model_pipeline = pipeline.Pipeline([("onehot", onehot),
                                    ("Modelo", grid)])

model_pipeline.fit(X_train,y_train)
# %%
y_train_proba = model_pipeline.predict_proba(X_train)
y_test_proba = model_pipeline.predict_proba(X_test)

# %%
cohort = 0.5
y_pred = (y_train_proba[:,1]>cohort).astype(int)
y_pred
#%%
y_train_pred = (y_train_proba[:,1]>cohort).astype(int)
acc_train = metrics.accuracy_score(y_train, y_train_pred)
auc_train = metrics.roc_auc_score(y_train, y_train_proba[:,1])
precision_train = metrics.precision_score(y_train, y_train_pred)
recall_train = metrics.recall_score(y_train, y_train_pred)
# %%
y_test_pred = (y_test_proba[:,1]>cohort).astype(int)

acc_test = metrics.accuracy_score(y_test, y_test_pred)
auc_test = metrics.roc_auc_score(y_test, y_test_proba[:,1])
precision_test = metrics.precision_score(y_test,y_test_pred)
recall_test = metrics.recall_score(y_test,y_test_pred)
# %%
df_predict_train = ({"Acuracia" :[acc_train],
                    "Curva Roc" :[auc_train],
                    "Precisão" :[precision_train],
                    "Recall" :[recall_train]})
df_predict_train
# %%
df_predict_test =({"Acuracia":[acc_test],
                    "Curva Roc":[auc_test],
                    "Precisão":[precision_test],
                    "Recall":[recall_test]})
df_predict_test
#%%
pd.concat([df_predict_train,df_predict_test])
#%%
df_metrics = pd.DataFrame([df_predict_train, df_predict_test])
df_metrics
# %%
model_series = pd.Series({"modelo": model_pipeline,
                          "features": features,
                          "metrics": df_metrics
})
#%%
model_series.to_pickle("F:/igor/Python/Credit Card Fraud Detection/models/modelo_final.pkl")
# model_series.to_pickle("../../models/modelo_final.pkl")


# %%
