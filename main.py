import pandas as pd
import matplotlib.pyplot as plt

# load data For a CSV file (like our example)
df = pd.read_csv('serial1.3-2025-10-22_09-35-11 - Second Charge.log')

#df = pd.read_csv('data.txt', sep='\t') #For .txt files
print(df.head())