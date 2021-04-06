
import matplotlib.pyplot as plt
import numpy as np


labels = ["Direct", "Container", "VM"]
Cal = [2.01, 2.06, 6.82]
function_time = [1.83,  1.84, 25.02]
trap_time = [413.83,  418.74, 695.52]

x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, Cal, width, label='operation')
rects2 = ax.bar(x, function_time, width, label='function')
rects3 = ax.bar(x + width, trap_time, width, label='syscall')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Average Time[nano-sec]')
ax.set_title('Different environment runtime comparison')
ax.set_xticks(x)
ax.set_xticklabels(labels)
plt.yscale("log")
ax.legend(loc='lower right')

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)


fig.tight_layout()

# plt.show()
plt.savefig('machine_comparison.png', bbox_inches='tight')