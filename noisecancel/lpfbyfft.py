# ruff: noqa: E402
# Noise removal using LPF by FFT (1st FFT, then remove high frequency)
# https://qiita.com/RyutoYoda/items/435787141cac5dd9eed7
# Get adventurers.wav from https://www.music-note.jp/bgm/fantasy.html
# %%
import matplotlib.pyplot as plt
from scipy.io import wavfile

filename = "adventurers.wav"
sample_rate, data = wavfile.read(filename)
# In case of multichannel (stereo) wav, then get the left channel only.
if len(data.shape) > 1:
    data = data[:, 0]

plt.rcdefaults()
# plt.style.use("fivethirtyeight")
plt.rcParams["font.family"] = "Source Han Code JP"  # In order to use Japanese font
fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(data)
ax.set(
    title="オリジナル波形",
    xlabel="サンプル ($t$)",
    ylabel="振幅 ($f(t)$)",
)
plt.show()

# %%
import numpy as np
from scipy.fft import fft

data_fft = fft(data)
# fftfreq computes the absolute frequency (Hz) of fft
frequencies = np.fft.fftfreq(len(data_fft), 1 / sample_rate)

# Band cut filter?
threshold_frequency_low = 4000
threshold_frequency_high = 24000
noise_indices = (np.abs(frequencies) > threshold_frequency_low) & (
    np.abs(frequencies) < threshold_frequency_high
)
data_fft_orig = data_fft.copy()
data_fft[noise_indices] = 0

plt.rcdefaults()
plt.rcParams["font.family"] = "Source Han Code JP"  # In order to use Japanese font
fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True)
axs[0].semilogy(np.abs(frequencies), np.abs(data_fft_orig))
axs[0].set_title("オリジナル周波数成分")
axs[0].set_ylabel("$| F(\\omega) |$")
axs[1].semilogy(np.abs(frequencies), np.abs(data_fft))
axs[1].set_title("バンドパス処理した周波数成分")
axs[1].set_ylabel("$| F(\\omega) |$")
axs[1].set_xlabel("周波数 $\\omega$ (Hz)")
plt.show()

# %%
from scipy.fft import ifft

noise_signal = np.real(ifft(data_fft_orig * noise_indices))
plt.rcdefaults()
plt.rcParams["font.family"] = "Source Han Code JP"  # In order to use Japanese font
fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(data, label="Original", alpha=0.5)
ax.plot(np.real(ifft(data_fft)), label="Cleaned", alpha=0.5)
ax.plot(noise_signal, label="Noise", color="red")
ax.set(
    title="ノイズ除去後の波形",
    xlabel="サンプル ($t$)",
    ylabel="振幅 ($f(t)$)",
)
ax.legend(loc="upper right", framealpha=0.7)
plt.show()

# %%
original_file = "original_adventurers.wav"
wavfile.write(original_file, sample_rate, data)
# ノイズ除去後の音声データをファイルとして保存
cleaned_file = "cleaned_adventurers.wav"
wavfile.write(cleaned_file, sample_rate, np.real(ifft(data_fft)).astype(np.int16))
