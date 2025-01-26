import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Initialize a dictionary to store all data
all_data = {
    'sample_num': [],
    'file_num': [],
    'sensor_position': [],
    'sensor_value': []
}

# Process Data1 to Data248
for i in range(1, 249):
    try:
        df = pd.read_csv(f'Data{i}.csv')
        
        all_data['sample_num'].extend(df["sample num"])
        all_data['file_num'].extend([i] * len(df))
        all_data['sensor_position'].extend(df["sensor position"])
        all_data['sensor_value'].extend(df["sensor value"])

        print(f"Processed Data{i}")
    except FileNotFoundError:
        print(f"Data{i}.csv not found. Skipping...")
    except Exception as e:
        print(f"Error processing Data{i}.csv: {str(e)}")

# Create a DataFrame from the combined data
combined_df = pd.DataFrame(all_data)

# Pivot the data to create columns for each sensor
pivoted_df = combined_df.pivot_table(
    values='sensor_value', 
    index=['file_num', 'sample_num'], 
    columns='sensor_position', 
    aggfunc='first'
).reset_index()

# Save all data to a single CSV file
pivoted_df.to_csv("all_data_combined.csv", index=False)
print("All data saved to all_data_combined.csv")

# Print some statistics
print(f"Total rows in combined data: {len(pivoted_df)}")
print(f"Number of unique files processed: {pivoted_df['file_num'].nunique()}")
print(f"Columns in the final dataset: {', '.join(pivoted_df.columns)}")
