import numpy as np
import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D']
values1 = [5, 7, 8, 6]  # First dataset
values2 = [6, 9, 5, 8]  # Second dataset
values3 = [4, 6, 7, 5]  # Third dataset

# Number of categories
n = len(categories)

# X-axis positions
x = np.arange(n)

# Width of each bar
bar_width = 0.25

# Plotting the bars (shift each dataset)
plt.bar(x, values1, width=bar_width, label='Dataset 1')
plt.bar(x + bar_width, values2, width=bar_width, label='Dataset 2')
plt.bar(x + 2 * bar_width, values3, width=bar_width, label='Dataset 3')

# Labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Multiple Bar Graph Example')
plt.xticks(x + bar_width, categories)
plt.legend()

# Show the plot
plt.show()
