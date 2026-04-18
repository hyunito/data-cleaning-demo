import pandas as pd
import numpy as np

def convert_age_group_to_mean(age_str):
    # Handle missing or null values first
    if pd.isna(age_str) or age_str in ["(null)", "UNKNOWN", "unknown"]:
        return np.nan
    
    # 1. Handle ranges like "25-44"
    if "-" in str(age_str):
        parts = age_str.split("-")
        low = float(parts[0])
        high = float(parts[1])
        return (low + high) / 2
    
    # 2. Handle "less than" like "<18"
    # Realistic assumption: We treat this as 17 for the mean.
    if "<" in str(age_str):
        val = float(age_str.replace("<", ""))
        return val - 1
    
    # 3. Handle "greater than" like "65+"
    # Realistic assumption: We treat this as 65 for the mean.
    if "+" in str(age_str):
        val = float(age_str.replace("+", ""))
        return val
    
    # 4. If it's already a single number, just return it
    try:
        return float(age_str)
    except:
        return np.nan

def clean_age_data(file_path):
    df = pd.read_csv(file_path)
    
    # Apply the transformation to the perpetrator age group
    # We create a new column so the Whale can see the 'Before' and 'After'
    df['PERP_AGE_NUMERIC'] = df['PERP_AGE_GROUP'].apply(convert_age_group_to_mean)
    
    output_name = 'cleaned_age_numeric.csv'
    df.to_csv(output_name, index=False)
    
    print(f"Transformed PERP_AGE_GROUP into numerical means.")
    print(f"Sample: '25-44' -> {convert_age_group_to_mean('25-44')}")
    print(f"Sample: '18-24' -> {convert_age_group_to_mean('18-24')}")
    print(f"Saved to {output_name}")

if __name__ == "__main__":
    clean_age_data('dataset/NYPD_Shootings/ARCHIVED_NYPD_Shooting_Incident_Data_(Historic)_20260418.csv')