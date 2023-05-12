import sounddevice as sd
import wavio as wv
import datetime


freq = 44100
duration = 5 # in seconds

#recordings_dir = os.path.join('transcribe', '*')


print('Recording')
while True:
    ts = datetime.datetime.now()
    filename = ts.strftime("%H%M%S")

    # Start recorder with the given values of duration and sample frequency
    # PTL Note: I had to change the channels value in the original code to fix a bug
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

    # Record audio for the given number of seconds
    sd.wait()

    # Convert the NumPy array to audio file
    #wv.open(f"{filename}.wav", 'wb')
    wv.write("transcribe/"+filename+".wav", recording, freq, sampwidth=2)
