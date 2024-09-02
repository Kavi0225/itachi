from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.metrics import mean_squared_error

df = pd.read_csv('homeprices.csv')
df = df.dropna()
x = df[['area','bedroom','age']]
y = df.price

model = LinearRegression()

res = model.fit(x,y)
print(mean_squared_error(res))
print(model.predict([[2600,6,17]]))

