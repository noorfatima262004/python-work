# bar graph

import matplotlib.pyplot as plt

# Data
name = ["SA", "USA", "PAK", "RUS", "IND", "QTR", "TURKEY"]
age = [22, 22, 24, 26, 28, 30, 33]

plt.xlabel("Sibling", fontsize=15, color='blue', labelpad=10)  
plt.ylabel("Ages", fontsize=15, color='blue', labelpad=10)     

col = ['r', 'b', 'gray', 'lightblue', 'green', 'purple', 'orange']

bars = plt.bar(name, age, color=col, width=0.4, alpha=0.7, edgecolor='black', linewidth=2)  
plt.bar_label(bars)

# Title with padding
plt.title("Name Vs Age", fontsize=18, pad=20,color='red')

plt.show()


