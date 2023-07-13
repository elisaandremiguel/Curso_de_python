# -*- coding: utf8 -*-

import sounddevice
from scipy.io.wavfile import write


def record() -> None:
    """
    Grava o audio apartir do microfone
    """
    fs: int = 44_100
    seconds: int = int(input("Quantos segundos deseja gravar? "))
    print("Gravando...")
    record_voice = sounddevice.rec(int(seconds * fs), samplerate=fs, channels=2)
    sounddevice.wait()
    write("gravacao.wav", fs, record_voice)
    print("Gravação Finalizada.")


record()
