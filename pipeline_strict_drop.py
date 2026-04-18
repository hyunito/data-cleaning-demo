import pandas as pd
import numpy as np

def clean_strict_drop(file_path):
    print("Running Pipeline 1: Strict Drop...")
    df = pd.read_csv(file_path)
    df = df.replace("(null)", np.nan)
    
    # 1. Define the crucial columns we cannot have missing
    crucial_columns = ['PERP_RACE', 'PERP_SEX', 'PERP_AGE_GROUP', 'Latitude', 'Longitude']
    
    # 2. Drop any row that has a NaN in these specific columns
    df_cleaned = df.dropna(subset=crucial_columns)
    
    # 3. Save the result
    output_name = 'cleaned_strict_drop.csv'
    df_cleaned.to_csv(output_name, index=False)
    
    print(f"Original rows: {len(df)} | New rows: {len(df_cleaned)}")
    print(f"Saved to {output_name}\n")
    return df_cleaned

if __name__ == "__main__":
    clean_strict_drop('dataset/NYPD_Shootings/ARCHIVED_NYPD_Shooting_Incident_Data_(Historic)_20260418.csv')