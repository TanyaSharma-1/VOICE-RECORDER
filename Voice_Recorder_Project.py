import sounddevice
from scipy.io.wavfile import write
import threading
import numpy as np

class VoiceRecorder:
    def __init__(self):
        self.recording = None
        self.is_recording = False

    def start_recording(self, file):
        self.is_recording = True
        self.recording = sounddevice.rec(int(44100), samplerate=44100, channels=2)
        self.thread = threading.Thread(target=self.record, args=(file,))
        self.thread.start()

    def stop_recording(self):
        self.is_recording = False
        sounddevice.stop()

    def record(self, file):
        while self.is_recording:
            sounddevice.wait()
            recording = sounddevice.rec(int(44100), samplerate=44100, channels=2)
            self.recording = np.concatenate((self.recording, recording))
        write(file, 44100, self.recording)
        print("Recording Saved.")

    def run(self, file):
        print("Press Enter to start recording")
        input()
        print("Voice Recording Started... Press Enter to stop recording")
        self.start_recording(file)
        input()
        self.stop_recording()

# usage
recorder = VoiceRecorder()
recorder.run("Recording1.wav")