import pandas as pd
import os
from datetime import datetime

def calculate_hmo(data):
    # Convert dates to datetime for calculations
    data['Date Sold'] = pd.to_datetime(data['Date Sold'], errors='coerce')
    data['Date Acquired'] = pd.to_datetime(data['Date Acquired'], errors='coerce')

    # Calculate holding period in years
    data['Holding Period (Years)'] = (data['Date Sold'] - data['Date Acquired']).dt.days / 365.25

    # Determine HMO percentage based on holding period
    data['HMO %'] = data['Holding Period (Years)'].apply(lambda x: 0.4 if x >= 10 else 0.2)

    # Calculate HMO value
    data['HMO (EUR)'] = data['Proceeds (EUR)'] * data['HMO %']

    # Decide if HMO is advantageous
    data['Use HMO'] = data.apply(
        lambda row: row['HMO (EUR)'] > row['Cost (EUR)'] and row['HMO (EUR)'] > 0,
        axis=1
    )

    # Calculate realized gain
    data['Realized Gain (EUR)'] = data.apply(
        lambda row: row['Proceeds (EUR)'] - row['HMO (EUR)'] if row['Use HMO'] else row['Proceeds (EUR)'] - row['Cost (EUR)'],
        axis=1
    )

    return data

# Define input and output directories relative to the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(script_dir, 'input')
output_dir = os.path.join(script_dir, 'output')

# Ensure input and output directories exist
os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

# Add .gitignore rules to exclude input and output directories
with open(os.path.join(script_dir, '.gitignore'), 'a') as gitignore:
    gitignore.write('\n# Ignore input and output directories\ninput/\noutput/\n')

# Find the first file in the input directory
input_files = [f for f in os.listdir(input_dir) if f.endswith('.xlsx')]
if not input_files:
    raise FileNotFoundError("No Excel files found in the input directory.")

input_file_path = os.path.join(input_dir, input_files[0])

# Load the original file
data = pd.read_excel(input_file_path)

# Perform the calculations
data_with_hmo = calculate_hmo(data)

# Generate a timestamped output file name
timestamp = datetime.now().strftime('%y%m%d%H%M%S')
output_file_name = f"hmo_calculated_{timestamp}.xlsx"
output_file_path = os.path.join(output_dir, output_file_name)

# Save the updated file with calculations
data_with_hmo.to_excel(output_file_path, index=False)

print(f"Updated file saved to: {output_file_path}")
