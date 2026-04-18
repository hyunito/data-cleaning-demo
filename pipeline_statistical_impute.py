import pandas as pd
import numpy as np

def clean_statistical_impute(file_path):
    print("Running Pipeline 2: Statistical Imputation...")
    df = pd.read_csv(file_path)
    df = df.replace("(null)", np.nan)
    
    # 1. Impute Categorical columns with the Mode (Most frequent)
    for col in ['PERP_RACE', 'PERP_SEX', 'PERP_AGE_GROUP', 'LOC_OF_OCCUR_DESC']:
        mode_val = df[col].mode()[0]
        df[col] = df[col].fillna(mode_val)
        
    # 2. Impute Numerical columns with the Median
    for col in ['Latitude', 'Longitude', 'JURISDICTION_CODE']:
        median_val = df[col].median()
        df[col] = df[col].fillna(median_val)
        
    # 3. Save the result
    output_name = 'cleaned_statistical_impute.csv'
    df.to_csv(output_name, index=False)
    
    print(f"Original rows: {len(df)} | New rows: {len(df)}")
    print(f"Saved to {output_name}\n")
    return df

if __name__ == "__main__":
    clean_statistical_impute('dataset/NYPD_Shootings/ARCHIVED_NYPD_Shooting_Incident_Data_(Historic)_20260418.csv')