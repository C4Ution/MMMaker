import tempfile
from moviepy.editor import *


def extract_audio(video_path):
    """
    :param video_path: 영상에 쓰일 하이라이트 영상 경로 리스트
    :return: 영상에서 추출된 오디오 파일 경로
    """

    # Create random file name
    tf = tempfile.NamedTemporaryFile()

    audio_path = os.getcwd() + tf.name[4:] + ".wav"

    # Access video file
    video_clip = VideoFileClip(video_path)

    # Extract audio file
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path)

    return audio_path


def overwrite_audio(video_path, audio_path):

    return video_path

