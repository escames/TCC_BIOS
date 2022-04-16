import dalex as dx
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier

data = open('Fraud.csv')
print(data)
#df = pd.read_csv(data)
# print(df)

"""
X = df.drop(columns='isFraud')
y = df.isFraud

categorical_features = ['type', 'nameOrig', 'nameDest']
numerical_features = ['step', 'amount', 'oldbalanceOrg',
                      'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']

categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(transformers=[
    ('cat', categorical_transformer, categorical_features),
    ('num', 'passthrough', numerical_features)
])

clf = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', DecisionTreeClassifier(max_depth=7, random_state=123))
])

clf.fit(X, y)

exp = dx.Explainer(clf, X, y)

exp.model_performance().result

"""
