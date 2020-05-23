import wave
import numpy as np
from moviepy.editor import *
# import matplotlib.pyplot as plt
import scipy.io.wavfile as wave
from scipy.fftpack import fft



def extract_highlights():
    """
    :param file_paths: 동영상 경로 리스트
    :return: 추출한 하이라이트 동영상 경로 리스트
    """
    video_clip = VideoFileClip('/Users/hyeseongkim/Workspaces/Projects/MMMaker/SourceVideo.mp4')
    audio_clip = video_clip.audio
    audio_clip.write_audiofile('/Users/hyeseongkim/Workspaces/Projects/MMMaker/SourceWave.wav')
    source_wave = wave.read('/Users/hyeseongkim/Workspaces/Projects/MMMaker/SourceWave.wav')

    stereo_channel_wave = source_wave[1].T[1]
    normalize_wave = [(ele / 2 ** 8.) * 2 - 1 for ele in stereo_channel_wave]  # this is 8-bit track, now normalized on [-1,1)
    fourier_transform_wave = fft(normalize_wave)  # calculate fourier transform (complex numbers list)
#    plt.plot(fourier_transform_wave, 'r')
#    plt.show()

    normalize_time = len(fourier_transform_wave) / video_clip.duration

    argmax_frequency = np.argmax(fourier_transform_wave) / normalize_time
    argmin_frequency = np.argmin(fourier_transform_wave) / normalize_time

    max_highlight = video_clip.subclip(argmax_frequency - 0.5, argmax_frequency + 0.5)
    min_highlight = video_clip.subclip(argmin_frequency - 0.5, argmin_frequency + 0.5)

#    max_highlight.write_videofile("/Users/hyeseongkim/Workspaces/Projects/MMMaker/MaxHighlight.mp4")
#    min_highlight.write_videofile("/Users/hyeseongkim/Workspaces/Projects/MMMaker/MaxHighlight.mp4")
#    return file_paths

extract_highlights()