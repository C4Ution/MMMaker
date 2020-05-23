import wave
from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wave
from scipy.fftpack import fft


def extract_highlights():
    """
    :param file_paths: 동영상 경로 리스트
    :return: 추출한 하이라이트 동영상 경로 리스트
    """

#    source_video = AudioSegment.from_file('/Users/hyeseongkim/Workspaces/Projects/MMMaker/SourceVideo.mp4', format="mp4")
#    source_video.export('/Users/hyeseongkim/Workspaces/Projects/MMMaker/SourceWave.wav', format="wav")


    rate, source_wave = wave.read('/Users/hyeseongkim/Workspaces/Projects/MMMaker/SourceWave.wav')

#    return file_paths

extract_highlights()