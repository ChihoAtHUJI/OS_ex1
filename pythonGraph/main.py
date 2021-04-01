
import matplotlib.pyplot as plt
import numpy as np


labels = ["Direct", "Container", "VM"]
Cal = [1.98, 1.96, 6.82]
function_time = [1.61,  1.57, 25.02]
trap_time = [390.21,  388.49, 654.52]

x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, Cal, width, label='operation')
rects2 = ax.bar(x, function_time, width, label='function')
rects3 = ax.bar(x + width, trap_time, width, label='syscall')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Average Time(nanosec)')
ax.set_title('Compare time in different environments')
ax.set_xticks(x)
ax.set_xticklabels(labels)
plt.yscale("log")
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)


fig.tight_layout()

# plt.show()
plt.savefig('compare.png', bbox_inches='tight')