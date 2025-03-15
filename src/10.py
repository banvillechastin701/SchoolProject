import pandas as pd

def clean_data(df):
    # Drop rows with missing values in 'Grade' column
    df = df.dropna(subset=['Grade'])
    
    # Convert 'Grade' column to categorical data
    df['Grade'] = pd.Categorical(df['Grade'])
    
    # Group by 'Class' and calculate the mean of 'Grade'
    means = df.groupby('Class')['Grade'].mean()
    
    # Return the means as a list
    return means.tolist()