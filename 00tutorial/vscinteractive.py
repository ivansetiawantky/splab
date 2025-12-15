# From https://code.visualstudio.com/docs/python/jupyter-support-py
# The `# %%` marks a cell

# %%
msg = "Hello World"
print(msg)

# %%
# MARK: Testing print(msg)
#
# The above will be shown if minimap is enabled.
msg = "Hello again"
print(msg)

# %%
print(512)

# View->Command palette: >Jupyter: Create Interactive Window
#     Press Shift+Enter for newline. Press Enter to execute.
#
# View->Command palette: >Jupyter: Run Current File in Interactive Window

# %% [markdown]
# # 線形計画法
# ## subsection
# * グラフ描画

# %% [markdown]
# This is an inline math: $\LaTeX$, $v = f \cdot \lambda$. <br>
# This is a displayed math:
# $$
# \int_{-\infty}^{\infty} f(x) \mathrm{d} x.
# $$ <br>
# This is also displayed math:
# $$
# \int_{1}^{\infty} \frac{1}{x^2} \mathrm{d}x = 1
# $$
# $$
# E = mc^2. \tag{2002}
# $$
# This is also a displayed mathematics:
# $$
# \frac{\mu_0}{4\pi} \times \frac{i \mathrm{d}l \sin \theta}{r^2}
# $$
# For more example, see [my github's ivansetiawantky/ttslearn/notebooks/nblatexmemo.ipynb](https://github.com/ivansetiawantky/ttslearn/blob/6e2d2d96e96a037c222e934ab679c60dd22b47a8/notebooks/nblatexmemo.ipynb).

# %%
# MARK: start debugging with F9 here
a = 3.14
print(a)

# %%
# Execute below in python REPL:
# %matplotlib --list
#
# %matplotlib inline
import math

import numpy as np
from matplotlib import pyplot as plt

t = np.linspace(0, 2 * math.pi, 800)
a = np.sin(t)
plt.figure(figsize=(9, 6), dpi=75)
plt.plot(t, a, "r")

# %%
# To display in the host windows, then must do:
# 1. In Dockerfile/container: apt-get install python3-tk
# 2. In mac host: xhost + localhost
#    That is, activate x server (xquartz) in mac.
#    The xquartz->setting->security: authenticate authorization & allow connection from network client.
# 3. In python code, add: matplotlib.use("tkagg") and plt.show()
# 4. In terminal inside container: DISPLAY=host.docker.internal:0 python3 vscinteractive.py
#
# Note: ssh -X user@remotepc.ip.com, will display the user@remotepc.ip.com's UI into the client.
#
# import math

# import matplotlib

# matplotlib.use("TkAgg")
# import matplotlib.pyplot as plt
# import numpy as np

# t = np.linspace(0, 2 * math.pi, 800)
# a = np.sin(t)
# plt.figure(figsize=(9, 6), dpi=75)
# plt.plot(t, a, "r")
# plt.show()
