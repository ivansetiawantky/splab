# ruff: noqa: E402
# Testing of matplotlib EXPLICIT & IMPLICIT API.
# Be careful, in matplotlib, axes and axis are different things.
# %%
import matplotlib.pyplot as plt

fig, ax = plt.subplots()  # Obtain Figure and Axes explicitly
ax.plot([1, 2, 3], [4, 1, 2])  # Use ax object's plot method
ax.set_title("Explicit Plot")
plt.show()

# %%
plt.plot([1, 2, 3], [4, 1, 2])  # Plot in current Axes
plt.title("Implicit Plot")
plt.show()

# %%
# https://www.practicaldatascience.org/notebooks/class_5/week_1/1.4.5_explicit_vs_implicit_syntax.html
# Explicit syntax
# %config InlineBackend.figure_format = 'retina'
import matplotlib.pyplot as plt

# Create some data to plot
x = [1, 2, 3, 4, 5]
y1 = [1, -2, 3, -4, 5]
y2 = [0, 2, 4, 6, 8]
fig, (ax1, ax2) = plt.subplots(1, 2)  # nrows, ncols of axes
ax1.plot(x, y1)
ax2.plot(x, y2)
plt.show()

# %%
# Implicit syntax here. The last axes is ax2, so everything is plot here.
fig, (ax1, ax2) = plt.subplots(1, 2)  # nrows, ncols of axes
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()

# %%
# To fix the above issue, must Set Current Axes to ax1 (or ax2) using sca()
fig, (ax1, ax2) = plt.subplots(1, 2)
plt.sca(ax1)
plt.plot(x, y1)
plt.sca(ax2)
plt.plot(x, y2)
plt.show()

# %%
# The Lifecycle of a Plot
# https://matplotlib.org/stable/tutorials/lifecycle.html
# In the explicit object-oriented (OO) interface we directly utilize instances of axes.Axes
# to build up the visualization in an instance of figure.Figure.
# In the implicit interface, inspired by and modeled on MATLAB, we use a global state-based
# interface which is encapsulated in the pyplot module to plot to the "current Axes".
#
# Things to remember:
#   - The Figure is the final image, and may contain one or more Axes.
#   - The Axes represents an individual plot (not to be confused with Axis, which refers to
#     the x-, y-, or z-axis of a plot).
# We call methods that do the plotting directly from the Axes, which is good for customizing plot.
import matplotlib.pyplot as plt
import numpy as np


def currency(x, pos):
    """The two arguments are the value and tick position"""
    if x >= 1e6:
        s = f"${x * 1e-6:1.1f}M"
    else:
        s = f"${x * 1e-3:1.0f}K"
    return s


data = {
    "Barton LLC": 109438.50,
    "Frami, Hills and Schmidt": 103569.59,
    "Fritsch, Russel and Anderson": 112214.71,
    "Jerde-Hilpert": 112591.43,
    "Keeling LLC": 100934.30,
    "Koepp Ltd": 103660.54,
    "Kulas Inc": 137351.96,
    "Trantow-Barrows": 123381.38,
    "White-Trantow": 135841.99,
    "Will LLC": 104437.60,
}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)
# print(plt.style.available)
plt.rcdefaults()  # Reset to the default plot style/params
plt.style.use("fivethirtyeight")
# plt.style.use("ggplot")  # When not displayed, Restart jupyter kernel. NO, use plt.rcdefaults()
plt.rcParams.update({"figure.autolayout": True})
fig, ax = plt.subplots(figsize=(6, 8))  # in inches
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment="right")
ax.set(
    xlim=[-10000, 140000],
    xlabel="Total Revenue",
    ylabel="Company",
    title="Company Revenue",
)
ax.xaxis.set_major_formatter(currency)

# %%
# Combining multiple visualizations
import matplotlib.pyplot as plt
import numpy as np


def currency(x, pos):
    """The two arguments are the value and tick position"""
    if x >= 1e6:
        s = f"${x * 1e-6:1.1f}M"
    else:
        s = f"${x * 1e-3:1.0f}K"
    return s


data = {
    "Barton LLC": 109438.50,
    "Frami, Hills and Schmidt": 103569.59,
    "Fritsch, Russel and Anderson": 112214.71,
    "Jerde-Hilpert": 112591.43,
    "Keeling LLC": 100934.30,
    "Koepp Ltd": 103660.54,
    "Kulas Inc": 137351.96,
    "Trantow-Barrows": 123381.38,
    "White-Trantow": 135841.99,
    "Will LLC": 104437.60,
}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)

plt.rcdefaults()  # Reset to the default plot style/params
plt.style.use("fivethirtyeight")
plt.rcParams.update({"figure.autolayout": True})
fig, ax = plt.subplots(figsize=(8, 8))  # in inches
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment="right")

# Add a vertical line, here we set the style in the function call
ax.axvline(group_mean, ls="--", color="r", label="Average")

# Annotate new companies
for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize=10, verticalalignment="center")

# Now we move our title up since it's getting a little cramped
ax.title.set(y=1.05)

ax.set(
    xlim=[-10000, 140000],
    xlabel="Total Revenue",
    ylabel="Company",
    title="Company Revenue",
)
ax.xaxis.set_major_formatter(currency)
ax.set_xticks([0, 25e3, 50e3, 75e3, 100e3, 125e3])
fig.subplots_adjust(right=0.1)
plt.show()
# print(fig.canvas.get_supported_filetypes())
# sales.png, sales.jpg, sales.svg
# fig.savefig("sales.svg", transparent=False, dpi=80, bbox_inches="tight")

# %%
# https://pbpython.com/effective-matplotlib.html
print("Access the above URL")

# %%
# https://matplotlib.org/stable/users/explain/figure/api_interfaces.html
# Matplotlib Application Interfaces (APIs)
import matplotlib.pyplot as plt

plt.rcdefaults()  # Reset to the default plot style/params
# plt.style.use("fivethirtyeight")
plt.style.use("ggplot")
# plt.style.use("seaborn-v0_8")
# plt.style.use("dark_background")
# plt.style.use("Solarize_Light2")
plt.rcParams.update({"figure.autolayout": True})
# fig, axs = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(7, 4))
fig, axs = plt.subplots(nrows=1, ncols=2)
axs[0].plot([1, 2, 3], [0, 0.5, 0.2])
axs[1].plot([3, 2, 1], [0, 0.5, 0.2])
fig.suptitle("Explicit Interface", fontsize=20, fontweight="bold")
for i in range(2):
    axs[i].set(
        xlabel="Total Revenue" + str(i),
        ylabel="Company" + str(i),
        title="Company Revenue" + str(i),
    )
plt.show()

# Things to remember:
#   - The Figure is the final image, and may contain one or more Axes.
#   - The Axes represents an individual plot (not to be confused with Axis, which refers to
#     the x-, y-, or z-axis of a plot).
#
# Translating between the Axes interface (explicit) and the pyplot interface (implicit):
# Creating figures:
#   fig, axs = plt.subplots(1, 3)   VS plt.subplots()
# Plotting data:
#   axs[0].plot(x, y)               VS plt.plot(x, y)
# Getting properties:
#   label = axs[1].get_xlabel()     VS label = plt.xlabel()
# Setting properties:
#   axs[2].set_xlabel("time")       VS plt.xlabel("time")

# %%
# https://matplotlib.org/stable/users/explain/quick_start.html
import matplotlib.pyplot as plt

plt.rcdefaults()  # Reset to the default plot style/params
# plt.style.use("ggplot")
# plt.rcParams.update({"figure.autolayout": True})

# Matplotlib graphs data on Figure, each of which can contain one or more Axes,
# an area where points can be specified in terms of x-y coordinates (or theta-r in polar).
# The simplest way of creating a Figure with an Axes is using pyplot.subplots.
fig, ax = plt.subplots()

# We can then use Axes.plot to draw some data on the Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
# In case where all figures created in a code cell (Jupyter or VSCode interactive python) are shown,
# then below plt.show() can be left out.
# plt.show()

# %%
# a figure with one Axes on the left, and two on the right:
import matplotlib.pyplot as plt  # noqa: E402

plt.rcdefaults()  # Reset to the default plot style/params
fig, axs = plt.subplot_mosaic([["left", "right_top"], ["left", "right_bottom"]])
axs["left"].plot([1, 2, 3, 4], [1, 4, 2, 3])
axs["right_top"].plot([1, 2, 3, 4], [1, 4, 2, 3])
axs["right_bottom"].plot([1, 2, 3, 4], [1, 4, 2, 3])

# %%
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

plt.rcdefaults()
# plt.rcParams.update({"figure.autolayout": True})
fig, ax = plt.subplots(figsize=[5, 2.7])
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)
(line,) = ax.plot(t, s, lw=2)
ax.annotate(
    "local max",
    xy=(2, 1),
    xytext=(3, 1.5),
    arrowprops=dict(facecolor="black", shrink=0.05),
)
ax.set_ylim(-2, 2)
ax.set_xlabel(r"$t$")
ax.set_ylabel(r"$\cos(2\pi t)$")
ax.set_title(r"Plot of $\cos(2\pi t)$")

# %%
import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)
fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(7, 2.7), layout="constrained")
(l1,) = ax1.plot(t, s)
ax2 = ax1.twinx()
(l2,) = ax2.plot(t, range(len(t)), "C1")
ax2.legend([l1, l2], [r"$\cos(2\pi t)$ (left)", "Straight (right)"])

(l3,) = ax3.plot(t, s)
ax3.legend([l3], [r"$\cos(\alpha)$"], loc="upper right")
ax3.set_xlabel(r"$\alpha$ [rad] / $2\pi$")
ax4 = ax3.secondary_xaxis(
    "top", (lambda x: np.rad2deg(2 * np.pi * x), lambda x: np.deg2rad(x) / (2 * np.pi))
)
ax4.set_xlabel(r"$\alpha$ [°]")

# %%
# https://matplotlib.org/stable/tutorials/pyplot.html
import matplotlib.pyplot as plt

plt.rcdefaults()
fig, ax = plt.subplots(nrows=1, ncols=1)
ax.plot([1, 2, 3, 4], [1, 4, 9, 16], "ro")
# ax.set_axis
ax.set(
    xlim=[0, 6],
    ylim=[0, 20],
)
plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()
# evenly sampled time at 200ms intervals
t = np.arange(0.0, 5.0, 0.2)

# red dashes, blue squares and green triangles
fig, ax = plt.subplots(nrows=1, ncols=1)
ax.plot(t, t, "r--", t, t**2, "bs", t, t**3, "g^")
plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()
np.random.seed(42)
data = {"a": np.arange(50), "c": np.random.randint(0, 50, 50), "d": np.random.randn(50)}
data["b"] = data["a"] + 10 * np.random.randn(50)
data["d"] = np.abs(data["d"]) * 100

fig, ax = plt.subplots()
ax.scatter("a", "b", c="c", s="d", data=data)
ax.set(xlabel="entry a", ylabel="entry b")
plt.show()

# %%
import matplotlib.pyplot as plt

plt.rcdefaults()
names = ["group_a", "group_b", "group_c"]
values = [1, 10, 100]

fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(9, 3))
axs[0].bar(names, values)
axs[1].scatter(names, values)
(line,) = axs[2].plot(names, values, linewidth=8.0)
# line.set_antialiased(False)
# line.set_linewidth(5.0)
fig.suptitle("Categorical Plotting")
plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()


def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

fig, axs = plt.subplots(nrows=2, ncols=1)
axs[0].plot(t1, f(t1), "bo", t2, f(t2), "k")
axs[1].plot(t2, np.cos(2 * np.pi * t2), "r--")
plt.show()

# %%
# Working with text
import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()
plt.style.use("ggplot")
plt.rcParams.update({"figure.autolayout": True})

np.random.seed(42)
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

fig, ax = plt.subplots()
# the histogram of the data
n, bins, patches = ax.hist(x, 50, density=True, facecolor="g", alpha=0.75)

ax.set(
    xlabel="Smarts",
    ylabel="Probability",
    title="Histogram of IQ",
    xlim=[40, 160],
    ylim=[0, 0.03],
)
ax.text(55, 0.025, r"$\mu=100,\ \sigma=15$", fontsize=15, color="red")
ax.grid(True)
plt.show()

# %%
# Annotating text
import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()
# plt.style.use("ggplot")
# plt.rcParams.update({"figure.autolayout": True})
fig, ax = plt.subplots()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)
(line,) = ax.plot(t, s, lw=2)

ax.annotate(
    "local max",
    xy=(2, 1),
    xytext=(3, 1.5),
    arrowprops=dict(facecolor="black", shrink=0.05),
)
ax.set(
    ylim=[-2, 2],
)
plt.show()

# %%
# Logarithmic and other non-linear axis
# Fixing random state for reproducibility
import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()

np.random.seed(19680801)

# make up some data in the open interval (0, 1)
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
fig, axs = plt.subplots(nrows=2, ncols=2)

# linear
axs[0, 0].plot(x, y)
axs[0, 0].set_yscale("linear")
axs[0, 0].set_title("linear")
axs[0, 0].grid(True)

# log
axs[0, 1].plot(x, y)
axs[0, 1].set_yscale("log")
axs[0, 1].set_title("log")
axs[0, 1].grid(True)

# symmetric log
axs[1, 0].plot(x, y - y.mean())
axs[1, 0].set_yscale("symlog", linthresh=0.01)
axs[1, 0].set_title("symlog")
axs[1, 0].grid(True)

# logit
axs[1, 1].plot(x, y)
axs[1, 1].set_yscale("logit")
axs[1, 1].set_title("logit")
axs[1, 1].grid(True)
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
fig.subplots_adjust(
    top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35
)

plt.show()

# %%
# Good reading: https://realpython.com/python-matplotlib-guide/
#
#
# https://realpython.com/python-matplotlib-guide/#appendix-b-interactive-mode
#
# If we start Python interactive window with Control-Enter (i.e. execute cell),
# then the `plt.rcParams["interactive"]` will become True.
# This means, we DON'T NEED to do `plt.show()`.
#
# If we Command+Shift+P (command palette) and `Python: Start Native Python REPL`,
# then the `plt.rcParams["interactive"]` will become False.
# This means, we NEED to do `plt.show()`.
# NATIVE REPL will open in xquartz new window, whether it is interactive or not.
#
# Notably, interactive mode has nothing to do with what IDE you’re using,
# or whether you’ve enable inline plotting with something like
# jupyter notebook --matplotlib inline or %matplotlib.
import matplotlib.pyplot as plt

plt.rcdefaults()
print(plt.rcParams["interactive"])
plt.ioff()
print(plt.rcParams["interactive"])
plt.ion()
print(plt.rcParams["interactive"])
plt.rcdefaults()
plt.plot([1, 2, 3], [1, 4, 9])
# Below plt.show() is required in case we use of ioff()
# plt.show()

# %%
import matplotlib.pyplot as plt

plt.rcdefaults()
fig, _ = plt.subplots()
print("type(fig) is:")
type(fig)

one_tick = fig.axes[0].yaxis.get_major_ticks()[0]
print("type(one_tick) is:")
type(one_tick)

plt.plot([1, 2, 3], [4, 9, 16])
plt.title("My Title")
# Try to press F12 on title, and see that it will show set_title

# %%
import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()
plt.style.use("bmh")
# print(plt.style.available)
rng = np.arange(50)
rnd = np.random.randint(0, 10, size=(3, rng.size))
yrs = 1950 + rng
fig, ax = plt.subplots(figsize=(5, 3))
# type(ax)
ax.stackplot(yrs, rng + rnd, labels=["Eastasia", "Eurasia", "Oceania"])
ax.set_title("Combined debt growth over time")
ax.legend(loc="upper left")
ax.set_ylabel("Total debt")
ax.set_xlim(xmin=yrs[0], xmax=yrs[-1])
fig.tight_layout()

# %%
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable

plt.rcdefaults()
x = np.diag(np.arange(2, 12))[::-1]
x[np.diag_indices_from(x[::-1])] = np.arange(2, 12)
x2 = np.arange(x.size).reshape(x.shape)

sides = ("left", "right", "top", "bottom")
nolabels = {s: False for s in sides}
nolabels.update({"label%s" % s: False for s in sides})
# print(nolabels)

with plt.rc_context(rc={"axes.grid": False}):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
    ax1.matshow(x)
    img2 = ax2.matshow(x2, cmap="RdYlGn_r")
    for ax in (ax1, ax2):
        ax.tick_params(axis="both", which="both", **nolabels)
    for i, j in zip(*x.nonzero()):
        ax1.text(j, i, x[i, j], color="white", ha="center", va="center")

    divider = make_axes_locatable(ax2)
    cax = divider.append_axes("right", size="5%", pad=0)
    plt.colorbar(img2, cax=cax, ax=[ax1, ax2])
    fig.suptitle("Heatmaps with `Axes.matshow`", fontsize=16)

plt.show()

# %%
# Mixing pandas plot with matplotlib stateless Axes (see the line ax = plt.gca())
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import numpy as np
import pandas as pd

plt.rcdefaults()
url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS"
vix = (
    pd.read_csv(
        url,
        index_col=0,
        parse_dates=True,
        na_values=".",
        date_format="%Y-%m-%d",
    )
    .squeeze()
    .dropna()
)
ma = vix.rolling("90D").mean()
state = pd.cut(ma, bins=[-np.inf, 14, 18, 24, np.inf], labels=range(4))

cmap = plt.get_cmap("RdYlGn_r")
ma.plot(color="black", linewidth=1.5, marker="", figsize=(8, 4), label="VIX 90D MA")

ax = plt.gca()  # Get the current Axes that ma.plot() references
ax.set_xlabel("")
ax.set_ylabel("90D moving average: CBOE VIX")
ax.set_title("Volatility Regime State")
ax.grid(False)
ax.set_xlim(xmin=ma.index[0], xmax=ma.index[-1])

trans = mtransforms.blended_transform_factory(ax.transData, ax.transAxes)
for i, color in enumerate(cmap([0.2, 0.4, 0.6, 0.8])):
    ax.fill_between(ma.index, 0, 1, where=state == i, facecolor=color, transform=trans)

ax.axhline(
    vix.mean(),
    linestyle="dashed",
    color="xkcd:dark grey",
    alpha=0.6,
    label="Full-period mean",
    marker="",
)
# ax.legend(loc="upper center")
ax.legend(loc="upper left")
