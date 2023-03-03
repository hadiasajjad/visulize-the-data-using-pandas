import pandas as pd



import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('HR.csv');

"""

#### Histogram


x = df["market_segment_type"]
plt.hist(x)
plt.xlabel("market_segment_type")
plt.show()

########## Scatter Plot

x = df["lead_time"]
y = df["avg_price_per_room"]
plt.scatter(x, y)
plt.xlabel("lead_time")
plt.ylabel("avg_price_per_room")
plt.show()

"""
####### Bar Chart

vv = (df.groupby('type_of_meal_plan').agg(["count"]))
x = np.array(["A", "B", "C", "D"])
vvv = vv["Booking_ID"]["count"]
y = np.array([vvv[0], vvv[1], vvv[2], vvv[3]])


plt.bar(x ,y, color = "hotpink", width = 0.5)
plt.show()



