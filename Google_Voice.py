import speech_recognition
import sys
from time import monotonic


def command():

    REC = speech_recognition.Recognizer()
    MIC = speech_recognition.Microphone()
    with speech_recognition.Microphone() as MIC:
        REC.pause_threshold = 1
        REC.adjust_for_ambient_noise(MIC, duration=1)
        AUDIO = REC.listen(MIC)

    try:

        Input = REC.recognize_google(AUDIO, language="ru-RU").lower()
        print(Input)
    except speech_recognition.UnknownValueError:
        Input = command()

    except speech_recognition.RequestError:
        import Vosk_Voice

    return Input


def Reactions(Input):
    Time = monotonic()

    if "солнцепёк" in Input:
        print(Input)
        if monotonic() - Time < 60:
            if "просто хаос" in Input:
                print(Input)
                import Delete
                import Block_Deblock
            elif "отменяю" in Input:
                print(Input)
                sys.exit()
        else:
            Reactions()

    else:
        if "остановить запуск" in Input:
            print(Input)
            sys.exit()


while True:
    Reactions(command())
