import matplotlib.pyplot as plt

def calculate_amdahl(s, n):
    # Use amdahl's law to calculate speedup and efficiency for a
    # given serial fraction s and a number of cores n
    speedup = 1. / (s + ((1.- s)/n))
    efficiency = speedup / n
    return speedup, efficiency

if __name__ == "__main__":
    cores = range(1, 129)
    serial = 0.1
    results = [calculate_amdahl(serial, core) for core in cores]
    speedups = [speedup for (speedup, efficiency) in results]
    efficiencies = [efficiency for (speedup, efficiency) in results]
    plt.figure()
    plt.plot(cores, speedups)
    plt.xlabel('# Cores')
    plt.ylabel('Speedup')
    plt.title('Cores vs Speedup for Amdahl\'s law w/ serial fraction 10%')
    plt.savefig('speedup.png')
    plt.figure()
    plt.plot(cores, efficiencies)
    plt.xlabel('# Cores')
    plt.ylabel('Efficiency')
    plt.title('Cores vs Efficiency for Amdahl\'s law w/ serial fraction 10%')
    plt.savefig('efficiency.png')

