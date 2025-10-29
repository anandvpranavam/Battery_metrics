import pandas as pd
import matplotlib.pyplot as plt

# Define column names based on your description
column_names = ['raw_time', 'voltage', 'ampere', 'soc', 'unknown']
# load data For a CSV file (like our example)
df = pd.read_csv('serial1.3-2025-10-22_09-35-11 - Second Charge.log', header=None, names=column_names)
#df = pd.read_csv('data.txt', sep='\t') #For .txt files
print(df.head())


# # 1. Create a figure and an axes (the "canvas" for our plot)
# plt.figure(figsize=(10, 6))  # Sets the size of the plot (width, height in inches)
# # 2. Plot the data
# # plt.plot(x-axis, y-axis)
# plt.plot(df['raw_time'], df['voltage'], marker='o', linestyle='-')
# # 3. Add labels and a title
# plt.title('Voltage Vs Time')
# plt.xlabel('Time')
# plt.ylabel('Voltage (V)')
# # 4. Add a grid for readability
# plt.grid(True)
# # 5. Display the plot
# plt.show()