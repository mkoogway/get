import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np

with open("settings.txt", "r") as settings:
    time = float(settings.readline())
    period = float(settings.readline())
    step = float(settings.readline())

data = []
with open("data.txt", "r") as input:
    t = []
    i = 0
    for line in input.readlines():
        data.append(float(line)*step)
        t.append(i)
        i += period

X = np.array(t[::50])
Y = np.array(data[::50])
Xnew = np.linspace(X.min(), X.max(), 300)
spline = make_interp_spline(X,Y,k=3)
Y_ = spline(Xnew)

fig, ax = plt.subplots()
line = ax.plot(X, Y, linewidth=1, marker='.', markersize=7, markerfacecolor='g')
ax.legend(line, ["line a "])

ax.set(xlabel='time, s', ylabel='voltage, V', title='RC charge')
ax.set_autoscale_on(True)

#ax.scatter(t[::100],data[::100], marker='.', color='g', s=64)
ax.grid(color='b', linestyle='-', linewidth='0.2', which='major')
ax.grid(color='b', linestyle='--', linewidth='0.1', which='minor')
ax.minorticks_on()
ax.text(0.8, 0.7, f"Charge time: {14} c", horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, bbox=dict(facecolor='red', alpha=0.5))
ax.text(0.8, 0.6, f"Discharge time: {26} c", horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, bbox=dict(facecolor='red', alpha=0.5))
ax.xaxis.set_label_position('bottom')
ax.axes.set_xlim(0)
ax.axes.set_ylim(0)
ax.yaxis.set_label_position('left')
fig.savefig("plt.svg")


plt.show()