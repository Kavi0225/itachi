from sklearn.linear_model import LinearRegression
import pandas as pd


df = pd.read_csv('homeprices.csv')
df = df.dropna()
x = df[['area','bedroom','age']]
y = df.price

model = LinearRegression()

model.fit(x,y)

print(model.predict([[2600,6,17]]))

