import wave
from pydub import AudioSegment
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


    source_wave = wave.read('/Users/hyeseongkim/Workspaces/Projects/MMMaker/SourceWave.wav')

    stereo_channel_wave = source_wave[1].T[1]
    normalize_wave = [(ele / 2 ** 8.) * 2 - 1 for ele in stereo_channel_wave]  # this is 8-bit track, b is now normalized on [-1,1)
    fourier_transform_wave = fft(normalize_wave)  # calculate fourier transform (complex numbers list)
    plt.plot(fourier_transform_wave, 'r')
    plt.show()

#    return file_paths

extract_highlights()