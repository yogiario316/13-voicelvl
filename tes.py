import sounddevice as sd
import numpy as np

# Parameter untuk perekaman
SAMPLE_RATE = 44100  # Hz
DURATION = 2  # detik

def print_sound_level(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    print("Tingkat suara: {:.2f} dB".format(volume_norm))

def main():
    print("Mendeteksi tingkat suara. Tekan Ctrl+C untuk menghentikan.")
    with sd.InputStream(callback=print_sound_level, channels=1, samplerate=SAMPLE_RATE):
        sd.sleep(int(DURATION * 2000))

if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Pendeteksian dihentikan.")

