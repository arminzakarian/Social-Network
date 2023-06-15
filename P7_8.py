import matplotlib.pyplot as plt
from collections import deque

file_path = 'email-Eu-core.txt'

def calculate_degree_distribution(file_path):
    in_degrees = {}
    out_degrees = {}

    with open(file_path, 'r') as file:
        for line in file:
            sender, receiver = map(int, line.strip().split())

            out_degrees[sender] = out_degrees.get(sender, 0) + 1
            in_degrees[receiver] = in_degrees.get(receiver, 0) + 1

    in_degree_values = list(in_degrees.values())
    out_degree_values = list(out_degrees.values())

    return in_degree_values, out_degree_values

in_degree_values, out_degree_values = calculate_degree_distribution(file_path)
print('>> Problem 7 and 8 Results:')
plt.hist(in_degree_values, bins=10, color='black')
plt.title('In_Degree Distribution1')
plt.xlabel('In_Degree')
plt.ylabel('Count')
plt.show()

plt.hist(out_degree_values, bins=10, color='black')
plt.title('Out_Degree Distribution1')
plt.xlabel('Out_Degree')
plt.ylabel('Count')
plt.show()
print('** Done **')