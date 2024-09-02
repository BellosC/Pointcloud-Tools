import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_pointcloud_distances(filenames):
    """
    Load the last column (C2C absolute distances) from multiple point cloud ASCII files.
    
    Args:
    filenames (list of str): List of file paths to the point cloud ASCII files.
    
    Returns:
    dict: A dictionary where keys are filenames and values are the C2C absolute distances.
    """
    distances = {}
    for filename in filenames:
        data = pd.read_csv(filename, delim_whitespace=True, header=None)
        distances[filename] = data.iloc[:, -1].abs()
    return distances

def compute_statistics(distances):
    """
    Compute the mean and standard deviation of C2C distances for each point cloud.
    
    Args:
    distances (dict): A dictionary of C2C distances.
    
    Returns:
    pd.DataFrame: A DataFrame containing filenames, means, and standard deviations.
    """
    stats = []
    for filename, values in distances.items():
        mean_distance = values.mean()
        std_dev_distance = values.std()
        stats.append((filename, mean_distance, std_dev_distance))
    
    return pd.DataFrame(stats, columns=['Filename', 'Mean C2C Distance', 'Standard Deviation'])

def plot_accuracy_comparison(stats):
    """
    Plot a bar chart comparing the accuracy of different point clouds based on mean C2C distances.
    
    Args:
    stats (pd.DataFrame): A DataFrame containing filenames, means, and standard deviations.
    """
    labels = ["GeoSLAM", "iPhone 15 Pro Max", "Livox Horizon based system", "NavVis VLX 3", "FARO FOCUS 3D"]
    plt.figure(figsize=(10, 6))
    plt.bar(labels, stats['Mean C2C Distance'], yerr=stats['Standard Deviation'], 
            capsize=5, color='skyblue', edgecolor='black')
    
    plt.xlabel('Point Cloud')
    plt.ylabel('Mean C2C Distance (with Standard Deviation)')
    plt.title('Accuracy Comparison of Point Clouds')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Example usage:
filenames = [
    r'C:\Users\proje\Desktop\costas\AgApostoloi\filter-95\1.geoslam\filtered-geoslam.txt',
    r'C:\Users\proje\Desktop\costas\AgApostoloi\filter-95\2.iphone\filtered-iphone15.txt',
    r'C:\Users\proje\Desktop\costas\AgApostoloi\filter-95\3.livox\filtered-livox.txt',
    r'C:\Users\proje\Desktop\costas\AgApostoloi\filter-95\4.navvis\filtered-navvis.txt',
    r'C:\Users\proje\Desktop\costas\AgApostoloi\filter-95\5.faro\filtered-faro.txt'
]

# Load distances from all point clouds
distances = load_pointcloud_distances(filenames)

# Compute statistics (mean and standard deviation)
stats = compute_statistics(distances)

# Plot the accuracy comparison
plot_accuracy_comparison(stats)
