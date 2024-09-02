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
    
    # Step 8: Plot histograms with adaptive binning and dynamic axis scaling
    plt.figure(figsize=(14, 7))

    # Function to calculate optimal number of bins using Freedman-Diaconis rule
    def optimal_bins(data):
        q25, q75 = np.percentile(data, [25, 75])
        iqr = q75 - q25
        bin_width = 2 * iqr * len(data) ** (-1/3)
        if bin_width == 0:
            return 10  # Fallback to 10 bins if IQR is zero
        bins = int(np.ceil((data.max() - data.min()) / bin_width))
        return bins

    # Histogram before filtering
    plt.subplot(1, 2, 1)
    bins_before = optimal_bins(last_column)
    plt.hist(last_column, bins=bins_before, edgecolor='black', color='skyblue')
    plt.title('Before Filtering')
    plt.xlabel('C2C Differences')
    plt.ylabel('Number of Points')
    plt.grid(True, linestyle='--', alpha=0.7)

    # Dynamic x-axis limits with padding
    padding = (last_column.max() - last_column.min()) * 0.05  # 5% padding on each side
    plt.xlim(last_column.min() - padding, last_column.max() + padding)

    # Histogram after filtering
    plt.subplot(1, 2, 2)
    bins_after = optimal_bins(filtered_data.iloc[:, -1])
    plt.hist(filtered_data.iloc[:, -1], bins=bins_after, edgecolor='black', color='salmon')
    plt.title('After Filtering')
    plt.xlabel('C2C Differences')
    plt.ylabel('Number of Points')
    plt.grid(True, linestyle='--', alpha=0.7)

    # Dynamic x-axis limits with padding
    filtered_min = filtered_data.iloc[:, -1].min()
    filtered_max = filtered_data.iloc[:, -1].max()
    padding_filtered = (filtered_max - filtered_min) * 0.05  # 5% padding on each side
    plt.xlim(filtered_min - padding_filtered, filtered_max + padding_filtered)

    # Add a title for the whole figure
    plt.suptitle('Pointcloud from Geoslam', fontsize=16)

    # Display the plots
    plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust layout to accommodate the title
    plt.show()

# Example usage:
filter_gaussian(
    r'C:\Users\proje\Desktop\costas\AgApostoloi\filter-95\geoslam.txt',
    r'C:\Users\proje\Desktop\costas\AgApostoloi\filter-95\filtered-geoslam.txt'
)
