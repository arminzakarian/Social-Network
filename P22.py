import numpy as np
import matplotlib.pyplot as plt

dataset = np.loadtxt("soc-Epinions1.txt", delimiter='\t', skiprows=4)

in_degree_counts = {}
out_degree_counts = {}

for edge in dataset:
    source = int(edge[0])
    target = int(edge[1])

    # Update in-degree counts
    if target in in_degree_counts:
        in_degree_counts[target] += 1
    else:
        in_degree_counts[target] = 1

    # Update out-degree counts
    if source in out_degree_counts:
        out_degree_counts[source] += 1
    else:
        out_degree_counts[source] = 1

# Calculate the frequencies of in-degree and out-degree
in_degree_freq = np.array(list(in_degree_counts.values()))
out_degree_freq = np.array(list(out_degree_counts.values()))

in_degree_freq.sort()
out_degree_freq.sort()

def fit_power_law(x, y):
    log_x = np.log10(x)
    log_y = np.log10(y)
    slope, _ = np.polyfit(log_x, log_y, 1)
    return slope

# In-Degree distribution
plt.scatter(range(1, len(in_degree_freq) + 1), in_degree_freq, color='b', s=5, label='In-degree')

# Out-degree distribution
plt.scatter(range(1, len(out_degree_freq) + 1), out_degree_freq, color='r', s=5, label='Out-degree')

in_degree_slope = fit_power_law(range(1, len(in_degree_freq) + 1), in_degree_freq)
out_degree_slope = fit_power_law(range(1, len(out_degree_freq) + 1), out_degree_freq)
print('>> Problem 22 Results:')
plt.xlabel('Degree (log scale)')
plt.ylabel('Frequency (log scale)')
plt.title('Power Law Distribution')
plt.legend()

plt.show()
print('** Done **')