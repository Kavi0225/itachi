import matplotlib.pyplot as plt
import pandas as pd

def petrol_price():

    df = pd.read_csv('petrol_price.csv')
    plt.figure(figsize=(1000,10))
    plt.plot(df.date,df.Delhi,color = "blue",linestyle="--",label = "Delhi")
    plt.plot(df.date,df.Telangana,color = "red",linestyle="-",label = "Telangana")
    plt.plot(df.date,df["Tamil Nadu"],color = "green",linestyle=":",label = "Tamil Nadu")
    plt.plot(df.date,df["Karnataka"],color = "purple",linestyle ="-",label = "Karnataka")
    plt.plot(df.date,df.Kerala,color = "orange",linestyle = "--",label ="Kerala")
    plt.title("Petrol_Price(INDIA)")
    plt.xlabel("year,month")
    plt.ylabel("price")

    # plt.xticks(range(2017,2022,2))

    plt.legend()
    plt.show()
print(petrol_price())
