import pyaudio
from array import array

FORMAT=pyaudio.paInt16
CHANNELS=2
RATE=44100
CHUNK=1024
SOUND_THRESHOLD = 3500 # You can adjust this value to change detection threshold

audio=pyaudio.PyAudio()

stream=audio.open(format=FORMAT,channels=CHANNELS, 
                  rate=RATE,
                  input=True,
                  frames_per_buffer=CHUNK)

print("-----------Start detection-------------")
while True:
    data=stream.read(CHUNK)
    data_chunk=array('h',data)
    vol=max(data_chunk)
    
    if(vol>=SOUND_THRESHOLD):
        print("sound detect vol:"+ str(vol))
