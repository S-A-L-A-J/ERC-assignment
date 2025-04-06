import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
from scipy.io import wavfile

fs, modulated = wavfile.read("modulated_noisy_audio.wav")
normal_modulated = modulated/np.max(np.abs(modulated))
time = np.arange(len(normal_modulated))/fs

fft_data =np.fft.fft(normal_modulated)
freqs = np.fft.fftfreq(len(normal_modulated), 1/fs)

positive_freqs = freqs[:len(freqs)//2]
positive_fft = np.abs(fft_data[:len(fft_data)//2])

plt.figure(figsize=(10,4))
plt.plot(positive_freqs, positive_fft)
plt.title("FFT")
plt.xlabel("f(Hz)")
plt.ylabel("Magnitude")
plt.grid()
plt.show()

peak_index = np.argsort(positive_fft)[-2:]
peak_freqs = positive_freqs[peak_index]
F = np.mean(peak_freqs)
print("Frequencies of the two largest peaks:", peak_freqs)
print("F:", F)

carrier_freq = np.cos(2 * np.pi*F* time)
demodulated_wave = normal_modulated * carrier_freq

def bandpass_filter(cutoff_freq, fs, order):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff_freq / nyquist
    b,a = butter(order, normal_cutoff, btype='low')
    return b, a

cutoff_freq = 4000
b,a = bandpass_filter(cutoff_freq, fs, 5)
filtered_wave = filtfilt(b, a, demodulated_wave)
cleaned_wave = filtered_wave/np.max(np.abs(filtered_wave))

wavfile.write("recovered_audio.wav", fs, (cleaned_wave * 32767).astype(np.int16))
plt.figure(figsize=(10,4))
plt.plot(time[:2000], normal_modulated[:2000], label="Modulated", alpha=0.5)
plt.plot(time[:2000], cleaned_wave[:2000], label="Recovered", alpha=0.8)
plt.title("Waveform Comparison")
plt.xlabel("T")
plt.legend()
plt.tight_layout()
plt.show()
