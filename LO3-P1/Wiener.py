import numpy as np
from scipy.io import wavfile
from scipy.signal import wiener

# Read the WAV file and extract sampling frequency (fs) and audio data (noise)
fs, noise = wavfile.read('noise.wav')

# Normalize the audio data to the range [-1, 1]
noise = noise / np.max(np.abs(noise))

# Apply Wiener filter for noise reduction
filtered_noise = wiener(noise, noise=0.1)

# Convert the filtered data back to 16-bit integer format
filtered_noise = (filtered_noise * 32767).astype(np.int16)

# Write the filtered audio data to a new WAV file
wavfile.write('filtered_noise.wav', fs, filtered_noise)
