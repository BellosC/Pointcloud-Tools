import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    
    # Step 8: Plot histograms
    plt.figure(figsize=(12, 6))

    # Histogram before filtering
    plt.subplot(1, 2, 1)
    plt.hist(last_column, bins=np.arange(0, 0.11, 0.01), edgecolor='black')
    plt.title('Before Filtering')
    plt.xlabel('C2C Differences')
    plt.ylabel('Number of Points')
    plt.xticks(np.arange(0, 0.11, 0.01))

    # Histogram after filtering
    plt.subplot(1, 2, 2)
    plt.hist(filtered_data.iloc[:, -1], bins=np.arange(0, 0.11, 0.01), edgecolor='black')
    plt.title('After Filtering')
    plt.xlabel('C2C Differences')
    plt.ylabel('Number of Points')
    plt.xticks(np.arange(0, 0.11, 0.01))

    # Add a title for the whole figure
    plt.suptitle('Pointcloud from blabla', fontsize=16)

    # Display the plots
    plt.tight_layout()
    plt.show()

# Example usage:
filter_gaussian(r'C:\Users\proje\Desktop\costas\AgApostoloi\filter-95\navvis.txt', r'C:\Users\proje\Desktop\costas\AgApostoloi\filter-95\filtered-navvis.txt')
