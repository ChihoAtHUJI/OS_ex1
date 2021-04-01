
import matplotlib.pyplot as plt
import numpy as np


labels = ['10^1', '10^2', '10^3', '10^4', '10^5','10^6', '10^7', '10^8', '10^9']
Cal = [0, 0.02, 0.03, 0.03, 0.03, 0.02, 0.04, 0.04, 0.03]
function_time = [0, 0.024, 0.023, 0.021, 0.036, 0.025, 0.034, 0.035, 0.037]
trap_time = [0.03, 0.044, 0.043, 0.041, 0.046, 0.035, 0.054, 0.045, 0.057]

x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, Cal, width, label='Calculation')
rects2 = ax.bar(x, function_time, width, label='Function')
rects3 = ax.bar(x + width, trap_time, width, label='Trap')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('time')
ax.set_title('Compare time')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)


fig.tight_layout()

# plt.show()
plt.savefig('compare.png', bbox_inches='tight')