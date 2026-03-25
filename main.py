import matplotlib.pyplot as plt
import pandas as pd

# loading the data from the CSV File
df = pd.read_csv("sales.csv")

print("Sales Data:")
print(df.head())