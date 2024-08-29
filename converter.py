import pandas as pd
import numpy as np

def filter_gaussian(input_filename, output_filename):
    # Step 1: Read the file
    data = pd.read_csv(input_filename, delim_whitespace=True, header=None)
    
    # Step 2: Extract the last column
    last_column = data.iloc[:, -1]
    
    # Step 3: Calculate mean and standard deviation
    mean = last_column.mean()
    std_dev = last_column.std()
    
    # Step 4: Calculate the Z-scores
    z_scores = (last_column - mean) / std_dev
    
    # Step 5: Determine the threshold for the top 5% (approx. 1.96 for 2-tailed 5%)
    threshold = np.percentile(np.abs(z_scores), 95)
    
    # Step 6: Filter out the rows where the Z-score is above the threshold
    filtered_data = data[np.abs(z_scores) <= threshold]
    
    # Step 7: Save the filtered data to a new file
    filtered_data.to_csv(output_filename, sep=' ', index=False, header=False)

# Example usage:
filter_gaussian(r'C:\Users\proje\Desktop\95\navvis.txt', r'C:\Users\proje\Desktop\95\filtered_output_navvis.txt')



