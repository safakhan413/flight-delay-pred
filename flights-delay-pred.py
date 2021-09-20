import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

flights=pd.read_csv("flights.csv")
print(flights.head(10))
flights.shape
sns.countplot(x="CANCELLATION_REASON",data=flights)
plt.show()
#Reason for Cancellation of flight: A - Airline/Carrier; B - Weather; C - National Air System; D - Security
sns.countplot(x="MONTH",hue="CANCELLATION_REASON",data=flights)
plt.show()
print(flights["CANCELLATION_REASON"].unique())
print