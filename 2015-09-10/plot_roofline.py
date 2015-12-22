import matplotlib.pyplot as plt
import numpy as np

def calculate_attainable_gflops(peak_bandwith, peak_gflops, operational_intensity):
    return min(peak_bandwith * operational_intensity, peak_gflops)

if __name__ == "__main__":
    peak_bandwith = 42.6
    peak_gflops = 120
    operational_intensities = np.linspace(0.125, 16, num = 500)
    attainable_perforances = [calculate_attainable_gflops(peak_bandwith, peak_gflops, oi) for oi in operational_intensities]
    plt.figure()
    plt.loglog(operational_intensities, attainable_perforances, basex=2, basey = 2)
    plt.xlabel('Operational Intensity')
    plt.ylabel('Attainable Performance')
    plt.title('Roofline Plot for Totient node')
    plt.savefig('roofline.png')
