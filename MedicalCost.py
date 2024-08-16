import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate


df = pd.read_csv('insurance.csv')
df = df.dropna()
# print(df)
lable_encode = LabelEncoder()

df_columns = ['sex','smoker','region']

for columns in df_columns:
    df[columns]=lable_encode.fit_transform(df[columns])

df.to_csv('insurance.csv', index= False)

# print(df.head())

x = df.drop('charges',axis='columns')
# print(x)

y = df['charges']
# print(y)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=.2,random_state=42)

model = LinearRegression()

model.fit(x_train,y_train)
predict = model.predict([[31,0,25.74,0,0,2]])
print(predict)
accuracy = model.score(x_test,y_test)
print(accuracy)
