import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LogLocator

flavor_texs = ["e", r"\mu", r"\tau"]
fs = 15

fname = "data/Visible_m1.txt"
dataf = open(fname, "r")
l = [float(x) for x in dataf.readline().split()]
a = int(l[0])
b = int(l[1])
g = l[2]
z = l[3]
gamma = l[4]
n_m1 = int(l[5])
m1s = []
for i in range(n_m1):
	m1s.append(l[6 + i])
dataf.close()

dts = ["Eb", "SM"]
for i in range(n_m1):
	dts.append("%g" % m1s[i])
dt = [(d, "f") for d in dts]
data = np.loadtxt(fname, dtype = dt, skiprows = 1)

for i in range(1, len(dts)):
	d = dts[i]
	try:
		if float(d) == 0:
			label = r"$m_1=\bf 0$"
		else:
			label = r"$m_1=%g{\rm\ eV}$" % float(d)
			label = r"$m_1=%g$" % float(d)
	except:
		label = r"${\rm %s}$" % d
	plt.plot(data["Eb"], data[d], label = label)

plt.xscale("log")

v = list(plt.axis())
v[0] = data["Eb"][0]
v[1] = data["Eb"][-1]
v[2] = 0
v[3] = 0.08
plt.axis(v)

plt.gca().xaxis.set_minor_locator(LogLocator(subs = "all", numticks = 1e5))
plt.gca().set_yticks(np.arange(v[2], v[3] + 1e-5, 0.005), minor = True)

plt.xlabel(r"$E_f{\rm\ [GeV]}$")
plt.ylabel(r"$\bar P_{%s %s}^{\rm vis}$" % (flavor_texs[a], flavor_texs[b]))

s = r"${\rm Visible}$"
s += "\n"
s += r"$g^{(\prime)}_{ij}="
p = np.log10(g)
if int(p) == p:
	s += r"10^{%i}" % p
else:
	s += r"%.1g\times10^{%i}" % (g / (10 ** p), p)
s += "$"
s += "\n"
s += r"$z=%g$" % z
s += "\n"
s += r"$\gamma=%g$" % gamma
plt.text(0.99, 0.99, s, ha = "right", va = "top", fontsize = fs, transform = plt.gca().transAxes)

# IceCube ROI
fc = "lightblue"
alpha = 0.4
plt.fill_between([1e4, 1e7], [v[2], v[2]], [v[3], v[3]], facecolor = fc, edgecolor = None, alpha = alpha, zorder = -10)
plt.fill_between(v[:2], [v[3] + 1, v[3] + 1], [v[3] + 2, v[3] + 2], facecolor = fc, edgecolor = "k", lw = 0.5, alpha = alpha)

plt.legend(fontsize = fs, loc = 4)

plt.savefig("fig/Visible_m1.pdf")

