
#  Sacttar plot

import matplotlib.pyplot as plt


name = ["SA", "USA", "PAK", "RUS", "IND", "QTR", "TURKEY"]
age = [22, 22, 24, 26, 28, 30, 33]
col = [22, 10, 20, 56, 40, 90, 60]
size = [100, 300, 340, 400, 150, 250, 600]

plt.scatter(name, age, c=col, s=size, cmap='viridis', alpha=0.7, edgecolor='black', linewidth=2)

plt.colorbar()

plt.xlabel("Country", fontsize=15, color='blue')
plt.ylabel("Ages", fontsize=15, color='blue')

plt.show()
