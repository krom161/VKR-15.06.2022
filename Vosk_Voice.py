from ast import Yield
from cgitb import text
import imp
from msilib.schema import Error
from vosk import Model, KaldiRecognizer
import pyaudio
import json
import sys
from time import monotonic

model = Model("vosk-model-small-ru-0.22")
REC = KaldiRecognizer(model, 16000)
PyA = pyaudio.PyAudio()
stream = PyA.open(
    format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000
)
stream.start_stream()


def AudioPrint():
    while True:
        data = stream.read(4000)
        if REC.AcceptWaveform(data) and len(data) > 0:
            Input = json.loads(REC.Result())
            if Input["text"]:
                yield Input["text"]
        else:
             import CombDelete


for text in AudioPrint():
    print(text)
    Time = monotonic()
    if monotonic() - Time < 60:
        if text == "яр с просто хаус":
            print(text)
            import Delete
            import Block_Deblock
        elif text == "отклоняю":
            print(text)
            sys.exit()
    elif text == "остановить запуск":
        print(text)
        sys.exit()
