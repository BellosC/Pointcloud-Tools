import matplotlib.pyplot as plt
import numpy as np

def get_mean_distances():
    devices = ['GeoSLAM Revo RT', 'iPhone 15 Pro Max', 'Livox based system', 'NavVis VLX 3', 'Leica BLK 360']
    c2c_mean = []
    m3c2_mean = []

    # Prompt user to enter the mean distance for each device for both methods
    print("Enter mean distances for Cloud-to-Cloud (C2C) method:")
    for device in devices:
        value = float(input(f"{device}: "))
        c2c_mean.append(value)

    print("\nEnter mean distances for M3C2 method:")
    for device in devices:
        value = float(input(f"{device}: "))
        m3c2_mean.append(value)

    return devices, c2c_mean, m3c2_mean

def plot_mean_distances(devices, c2c_mean, m3c2_mean):
    # Bar width
    bar_width = 0.35

    # Setting positions for bars
    r1 = np.arange(len(devices))
    r2 = [x + bar_width for x in r1]

    # Plotting
    plt.figure(figsize=(10, 6))

    plt.bar(r1, c2c_mean, color='blue', width=bar_width, edgecolor='grey', label='Cloud-to-Cloud Mean')
    plt.bar(r2, m3c2_mean, color='orange', width=bar_width, edgecolor='grey', label='M3C2 Mean')

    plt.xlabel('Device', fontweight='bold')
    plt.ylabel('Mean Distance', fontweight='bold')
    plt.title('Mean Distance Comparison: Cloud-to-Cloud vs M3C2')
    plt.title('Mean Distance Comparison: Cloud-to-Cloud vs M3C2\nPointcloud data from each device compared with pointcloud data from FARO FOCUS 3D used as reference')
    plt.xticks([r + bar_width/2 for r in range(len(devices))], devices)

    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    devices, c2c_mean, m3c2_mean = get_mean_distances()
    plot_mean_distances(devices, c2c_mean, m3c2_mean)
