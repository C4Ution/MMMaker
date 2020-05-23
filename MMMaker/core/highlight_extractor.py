import wave
from pydub import AudioSegment


def extract_highlights(file_paths):
    """
    :param file_paths: 동영상 경로 리스트
    :return: 추출한 하이라이트 동영상 경로 리스트
    """

    source_video = AudioSegment.from_file('./SourceVideo.mp4', format="mp4")
    source_video.export('./SourceWave.wav', format="wav")

    source_wave = wave.open('./SourceWave.wav', 'r')

    return file_paths
