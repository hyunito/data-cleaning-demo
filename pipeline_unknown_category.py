import pandas as pd
import numpy as np

def clean_unknown_category(file_path):
    print("Running Pipeline 3: Unknown Category Assignment...")
    df = pd.read_csv(file_path)
    df = df.replace("(null)", np.nan)
    
    # 1. Replace missing categorical data with the explicit string "UNKNOWN"
    categorical_cols = ['PERP_RACE', 'PERP_SEX', 'PERP_AGE_GROUP', 'LOC_OF_OCCUR_DESC', 'LOCATION_DESC']
    for col in categorical_cols:
        df[col] = df[col].fillna("UNKNOWN")
        
    # 2. For geographical missing data, we can't use "UNKNOWN", so we drop just those few rows
    df_cleaned = df.dropna(subset=['Latitude', 'Longitude'])
    
    # 3. Save the result
    output_name = 'cleaned_unknown_category.csv'
    df_cleaned.to_csv(output_name, index=False)
    
    print(f"Original rows: {len(df)} | New rows: {len(df_cleaned)}")
    print(f"Saved to {output_name}\n")
    return df_cleaned

if __name__ == "__main__":
    clean_unknown_category('dataset/NYPD_Shootings/ARCHIVED_NYPD_Shooting_Incident_Data_(Historic)_20260418.csv')