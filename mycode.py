import pandas as pd
import os

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

#Adding new row to data for second version
new_row = {'Name': 'David', 'Age': 40, 'City': 'Houston'}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

#Adding new row to data for third version
new_row = {'Name': 'Sher', 'Age': 25, 'City': 'London'}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

data_dir = 'data'
# To check if the directory exists and create it if it doesn't
os.makedirs(data_dir, exist_ok=True)

#Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the DataFrame to a CSV file
df.to_csv(file_path, index=False)

print(f"DataFrame saved to {file_path}")