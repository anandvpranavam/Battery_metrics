import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Define column names based on your description
column_names = ['raw_time', 'voltage', 'ampere', 'soc', 'unknown']
# load data For a CSV file (like our example)
df = pd.read_csv('serial1.3-2025-10-22_09-35-11 - Second Charge.log', header=None, names=column_names)
#df = pd.read_csv('data.txt', sep='\t') #For .txt files

# Create a new column named 'time' by slicing the 'raw_time' column
# .str lets us apply string functions
# [1:9] slices the string from index 1 up to (but not including) index 9
# df['time'] = df['raw_time'].str[1:9]
# **Convert the string column to a real datetime object**
# This is the most important step. Pandas will understand this as time.
df['time'] = pd.to_datetime(df['raw_time'].str[1:9], format='%H:%M:%S')
print(df.head())


# 1. Create a figure and an axes (the "canvas" for our plot)
plt.figure(figsize=(12, 6))  # Sets the size of the plot (width, height in inches)
# 2. Plot the data
# plt.plot(x-axis, y-axis)
plt.plot(df['time'], df['voltage'])
# 3. Add labels and a title
plt.title('Voltage Vs Time')
plt.xlabel('Time (HH:MM)')
plt.ylabel('Voltage (V)')
# 4. Add a grid for readability
plt.grid(True)

# --- SET 30-MINUTE X-AXIS ---
# Get the current axes
ax = plt.gca()
# Set the major ticks to be every 30 minutes
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=30))
# Set the format of the tick labels to show 'Hour:Minute'
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout() # Fits labels neatly in the figure

# Display the plot
plt.show()

# Save the plot
plt.savefig('voltage_plot_30min_interval.png')