import wave
import numpy as np
from moviepy.editor import *

import matplotlib.pyplot as plt
import scipy.io.wavfile as wave
from scipy.fftpack import fft



def extract_highlights():
    """
    :param file_paths: 동영상 경로 리스트
    :return: 추출한 하이라이트 동영상 경로 리스트
    """
    video_clip = VideoFileClip('/Users/hyeseongkim/Workspaces/Projects/MMMaker/SourceVideo.mp4')
    source_video = video_clip.audio
    source_video.write_audiofile('/Users/hyeseongkim/Workspaces/Projects/MMMaker/SourceWave.wav')


    source_wave = wave.read('/Users/hyeseongkim/Workspaces/Projects/MMMaker/SourceWave.wav')

    stereo_channel_wave = source_wave[1].T[1]
    normalize_wave = [(ele / 2 ** 8.) * 2 - 1 for ele in stereo_channel_wave]  # this is 8-bit track, now normalized on [-1,1)
    fourier_transform_wave = fft(normalize_wave)  # calculate fourier transform (complex numbers list)
#    plt.plot(fourier_transform_wave, 'r')
#    plt.show()


#    return file_paths

extract_highlights()