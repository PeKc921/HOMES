import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Files/Mall_Customers.csv', delimiter=',', encoding='utf-8')
print(df[df["Genre"] == "Female"]["Annual Income (k$)"].mean())
fe = df[df["Genre"] == "Female"]
ma = df[df["Genre"] == "Male"]
print(f"Female most spending score: \n{fe[fe["Spending Score (1-100)"] == fe["Spending Score (1-100)"].max()]}")
print(f"Male most spending score: \n{ma[ma["Spending Score (1-100)"] == ma["Spending Score (1-100)"].max()]}")

malesincome = pd.DataFrame({
    "Age": ma["Age"],
    "Annual Income (k$)": ma["Annual Income (k$)"]
})
malesincome = malesincome.set_index("Age")
plt.bar(ma["Age"], ma["Annual Income (k$)"], color = "crimson")
plt.bar(fe["Age"], fe["Annual Income (k$)"], color = "pink")
plt.xlabel('Age')
plt.ylabel('Annual Income')
plt.show()
