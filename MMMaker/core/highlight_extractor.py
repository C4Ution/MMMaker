import numpy as np
from moviepy.editor import VideoFileClip
import scipy.io.wavfile as wave
from scipy.fftpack import fft
from misc import get_random_name


HIGHLIGHT_LENGTH = 0.65


def extract_highlights(file_paths):
    """
    :param file_paths: 동영상 경로 리스트
    :return: 추출한 하이라이트 동영상 경로 리스트
    """

    max_highlights = []
    min_highlights = []

    for file_path in file_paths:
        video_clip = VideoFileClip(file_path)
        audio_clip = video_clip.audio
        src_audio_file_name = get_random_name('wav')
        audio_clip.write_audiofile(src_audio_file_name, codec='libx264', audio_codec='aac')
        source_wave = wave.read(src_audio_file_name)

        stereo_channel_wave = source_wave[1].T[1]
        normalize_wave = [(ele / 2 ** 8.) * 2 - 1 for ele in stereo_channel_wave]  # this is 8-bit track, now normalized on [-1,1)
        fourier_transform_wave = fft(normalize_wave)  # calculate fourier transform (complex numbers list)

        normalize_time = len(fourier_transform_wave) / video_clip.duration

        argmax_frequency = np.argmax(fourier_transform_wave) / normalize_time + 0.5
        argmin_frequency = np.argmin(abs(fourier_transform_wave)) / normalize_time + 0.5

        max_highlights.append(video_clip.subclip(argmax_frequency - (HIGHLIGHT_LENGTH/2), argmax_frequency + (HIGHLIGHT_LENGTH/2)))
        min_highlights.append(video_clip.subclip(argmin_frequency - (HIGHLIGHT_LENGTH/2), argmin_frequency + (HIGHLIGHT_LENGTH/2)))

#    max_highlight.write_videofile('MaxHighlight.mp4', codec='libx264', audio_codec='aac')
#    min_highlight.write_videofile('MinHighlight.mp4', codec='libx264', audio_codec='aac')
        video_clip.close()
    return max_highlights, min_highlights