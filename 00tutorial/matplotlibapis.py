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
