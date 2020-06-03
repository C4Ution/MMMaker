import numpy as np
from moviepy.editor import VideoFileClip
# import matplotlib.pyplot as plt
import scipy.io.wavfile as wave
from scipy.fftpack import fft
from misc import get_random_name


HIGHLIGHT_LENGTH = 0.65


def extract_highlights(file_paths):
    """
    :param file_paths: 동영상 경로 리스트
    :return: 추출한 하이라이트 동영상 경로 리스트
    """

    video_clip = VideoFileClip(file_paths)
    audio_clip = video_clip.audio
    src_audio_file_name = get_random_name('wav')
    audio_clip.write_audiofile(src_audio_file_name)
    source_wave = wave.read(src_audio_file_name)

    for file_path in file_paths:
        video_clip = VideoFileClip(file_path)
        audio_clip = video_clip.audio
        src_audio_file_name = get_random_name('wav')
        audio_clip.write_audiofile(src_audio_file_name)
        source_wave = wave.read(src_audio_file_name)

    normalize_time = len(fourier_transform_wave) / video_clip.duration

    argmax_frequency = np.argmax(fourier_transform_wave) / normalize_time + 0.5
    argmin_frequency = np.argmin(abs(fourier_transform_wave)) / normalize_time + 0.5


    max_highlight = video_clip.subclip(argmax_frequency - (HIGHLIGHT_LENGTH/2), argmax_frequency + (HIGHLIGHT_LENGTH/2))
    min_highlight = video_clip.subclip(argmin_frequency - (HIGHLIGHT_LENGTH/2), argmin_frequency + (HIGHLIGHT_LENGTH/2))

#    max_highlight.write_videofile('MaxHighlight.mp4')
#    min_highlight.write_videofile('MinHighlight.mp4')
    video_clip.close()
    return max_highlight, min_highlight