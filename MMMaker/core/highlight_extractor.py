import numpy as np
import scipy.io.wavfile as wave
from moviepy.editor import VideoFileClip
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
        audio_clip.write_audiofile(src_audio_file_name)
        source_wave = wave.read(src_audio_file_name)

        stereo_channel_wave = source_wave[1].T[1]
        normalize_wave = [(ele / 2 ** 8.) * 2 - 1 for ele in stereo_channel_wave]  # this is 8-bit track, now normalized on [-1,1)
        # fourier_transform_wave = fft(normalize_wave)  # calculate fourier transform (complex numbers list)
        fourier_transform_wave = normalize_wave
        normalize_time = len(fourier_transform_wave) / video_clip.duration

        argmax_frequency = np.argmax(fourier_transform_wave) / normalize_time
        argmin_frequency = np.argmin(fourier_transform_wave) / normalize_time

        max_highlight_path = max_highlights.append(get_random_name('mp4'))
        min_highlight_path = min_highlights.append(get_random_name('mp4'))

        start_max = argmax_frequency - (HIGHLIGHT_LENGTH/2)
        end_max = argmax_frequency + (HIGHLIGHT_LENGTH/2)

        if start_max < 0:
            end_max -= start_max
            start_max = 0
        elif end_max > video_clip.duration:
            start_max -= end_max - video_clip.duration
            end_max = video_clip.duration

        video_clip.subclip(start_max, end_max).write_videofile(max_highlights[-1], codec='libx264', audio_codec='aac')

        start_min = argmin_frequency - (HIGHLIGHT_LENGTH/2)
        end_min = argmin_frequency + (HIGHLIGHT_LENGTH/2)

        if start_min < 0:
            end_min -= start_min
            start_min = 0
        elif end_min > video_clip.duration:
            start_min -= end_min - video_clip.duration
            end_min = video_clip.duration

        video_clip.subclip(start_min, end_min).write_videofile(min_highlights[-1], codec='libx264', audio_codec='aac')

        video_clip.close()

    return max_highlights, min_highlights
