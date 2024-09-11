import matplotlib.pyplot as plt
import numpy as np

def get_std_deviations():
    devices = ['GeoSLAM Revo RT', 'iPhone 15 Pro Max', 'Livox based system', 'NavVis VLX 3', 'Leica BLK 360']
    c2c_std = []
    m3c2_std = []

    # Prompt user to enter the std deviation for each device for both methods
    print("Enter standard deviations for Cloud-to-Cloud (C2C) method:")
    for device in devices:
        value = float(input(f"{device}: "))
        c2c_std.append(value)

    print("\nEnter standard deviations for M3C2 method:")
    for device in devices:
        value = float(input(f"{device}: "))
        m3c2_std.append(value)

    return devices, c2c_std, m3c2_std

def plot_std_deviations(devices, c2c_std, m3c2_std):
    # Bar width
    bar_width = 0.35

    # Setting positions for bars
    r1 = np.arange(len(devices))
    r2 = [x + bar_width for x in r1]

    # Plotting
    plt.figure(figsize=(10, 6))

    plt.bar(r1, c2c_std, color='blue', width=bar_width, edgecolor='grey', label='Cloud-to-Cloud Std Dev')
    plt.bar(r2, m3c2_std, color='orange', width=bar_width, edgecolor='grey', label='M3C2 Std Dev')

    plt.xlabel('Device', fontweight='bold')
    plt.ylabel('Standard Deviation', fontweight='bold')
    plt.title('Standard Deviation Comparison: Cloud-to-Cloud vs M3C2')
    plt.title('Mean Distance Comparison: Cloud-to-Cloud vs M3C2\nPointcloud data from each device compared with pointcloud data from FARO FOCUS 3D used as reference')
    plt.xticks([r + bar_width/2 for r in range(len(devices))], devices)

    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    devices, c2c_std, m3c2_std = get_std_deviations()
    plot_std_deviations(devices, c2c_std, m3c2_std)
