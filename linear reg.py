import pandas as pd
import re
from sklearn import linear_model
import openpyxl
import math

# df = pd.read_excel(r'population.xlsx')
#
# reg = linear_model.LinearRegression()
#
# reg.fit(df[['Year']], df.Population)
#
# userint = int(input("enter the year to calculate population : "))
#
# res = float(reg.predict([[userint]]))
# print("the prediction result =" ,res)



#
# df = pd.read_csv('area_price.csv')
# print(df)
# reg = linear_model.LinearRegression()
#
# reg.fit(df[['area']],df.price)
#
# area = int(input(" enter the square feet whose price has to be predicted = "))
#
# res = reg.predict([[area]])
# print(" the prediction result is = " , res)
#


#
df = pd.read_csv('homeprices.csv')
print(df)

mreg = linear_model.LinearRegression()

# replace all the null or na values with the median data
df.bedroom = df.bedroom.fillna(df.bedroom.median())


# print(df)




mreg.fit(df[['area','age','bedroom']],df.price)

uarea = int(input("enter the area = "))
ubed = int(input("enter the bedrooms number  = "))
uage = int(input("enter the age of the flat = "))


# res = mreg.predict([[2600,3.0,20]])

res = mreg.predict([[uarea,ubed,uage]])
print(res)

co_ef = mreg.coef_
intercept = mreg.intercept_
print(co_ef,intercept)
df_out = pd.read_csv('new_area.csv')
op = mreg.predict(df_out)
df_out['price'] = op
print(df_out)
df_out.to_csv('new_area.csv',index=False)
print(" Complete ")
