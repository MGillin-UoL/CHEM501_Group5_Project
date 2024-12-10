import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load the CSV file [Insert your own directory here!]
file_name = r"INSERT YOUR OWN DIRECTORY HERE!"
data = pd.read_csv(file_name)

# Convert the Timestamp column to datetime
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Plot 1: Time vs Temperature
plt.figure(figsize=(10, 6))
plt.plot(data['Timestamp'], data['Temperature'], label='Temperature', color='red')
plt.xlabel('Time')
plt.ylabel('Temperature / °C')
plt.title('Time vs Temperature')

# Format x-axis to show hourly increments
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=1))  # Set hourly ticks
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))  # Format as HH:MM
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
#plt.grid()
plt.tight_layout()
plt.show()

# Plot 2: Time vs Gas
plt.figure(figsize=(10, 6))
plt.plot(data['Timestamp'], data['Gas'], label='Gas', color='blue')
plt.xlabel('Time')
plt.ylabel('Gas / Ω')
plt.title('Time vs Gas')

# Format x-axis to show hourly increments
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=1))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.xticks(rotation=45)
#plt.grid()
plt.tight_layout()
plt.show()

# Plot 3: Time vs Temperature and Gas with dual y-axes
fig, ax1 = plt.subplots(figsize=(10, 6))

# Primary y-axis (Temperature)
ax1.plot(data['Timestamp'], data['Temperature'], color='#0072B2', label='Temperature')
ax1.set_xlabel('Time')
ax1.set_ylabel('Temperature / °C', color='#0072B2')
ax1.tick_params(axis='y', labelcolor='#0072B2')
ax1.set_title('Time vs Temperature and Gas')
#ax1.grid()

# Format x-axis to show hourly increments
ax1.xaxis.set_major_locator(mdates.HourLocator(interval=1))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

# Secondary y-axis (Gas)
ax2 = ax1.twinx()
ax2.plot(data['Timestamp'], data['Gas'], color='#D55E00', label='Gas')
ax2.set_ylabel('Gas Resistance / Ω', color='#D55E00')
ax2.tick_params(axis='y', labelcolor='#D55E00')

# Rotate x-axis labels
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
