import paho.mqtt.subscribe as subscribe
import pandas as pd
import sqlite3
from datetime import datetime
import os

# List of topics to subscribe to
topics = ['Temp', 'Gas']

# MQTT broker hostname
hostname = "pf-eveoxy0ua6xhtbdyohag.cedalo.cloud"

# Specify the CSV file path
csv_directory = os.path.expanduser("~/mqtt_data")  # Save in the 'mqtt_data' folder in your home directory
os.makedirs(csv_directory, exist_ok=True)  # Ensure the directory exists
csv_filepath = os.path.join(csv_directory, "Collection_data.csv")  # Path to the CSV file
db_filepath = os.path.join(csv_directory, "mqtt_data_collection.db")  # Path to the SQLite database

# Check if the CSV file exists; if not, create it with column titles
if not os.path.isfile(csv_filepath):
    pd.DataFrame(columns=["Timestamp", "Temperature", "Gas"]).to_csv(csv_filepath, index=False)

print(f"CSV file is located at: {csv_filepath}")

# Initialize a dictionary to hold the data for each topic
data_dict = {"Temperature": None, "Gas": None}

while True:  # Continuously listen for data
    for topic in topics:
        try:
            # Subscribe to one topic at a time
            m = subscribe.simple(topic, hostname=hostname, retained=False, msg_count=1)
            payload = float(m.payload)  # Ensure payload is a float
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Update the corresponding entry in the data dictionary
            if topic == 'Temp':
                data_dict["Temperature"] = payload
            elif topic == 'Gas':
                data_dict["Gas"] = payload

            # If all values are collected, save them to the CSV
            if None not in data_dict.values():  # Only write when all topics have values
                # Create a DataFrame with the new data
                data = pd.DataFrame([{
                    "Timestamp": timestamp,
                    "Temperature": data_dict["Temperature"],
                    "Gas": data_dict["Gas"]
                }])

                # Append the new data to the CSV file
                data.to_csv(csv_filepath, mode='a', header=False, index=False)

                # Print data for monitoring
                print(f"Saved: {timestamp}, Temperature: {data_dict['Temperature']}, Gas: {data_dict['Gas']}")

                # Reset the dictionary for the next round of data
                data_dict = {"Temperature": None, "Gas": None}

        except ValueError:
            print(f"Error: Could not convert payload from {topic} to float.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(csv_filepath)

    # SQLite database connection
    conn = sqlite3.connect(db_filepath)

    try:
        # Save DataFrame to SQLite (creates table named 'mqtt_data_run2')
        df.to_sql('Collection_data.csv', conn, if_exists='replace', index=False)  # 'replace' overwrites existing table
        print(f"CSV data has been saved to SQLite table 'mqtt_data_collection.db'.")

    except Exception as e:
        print(f"Error while saving CSV to SQL: {e}")
    finally:
        conn.commit()
        conn.close()

    print("Database operation completed.")
