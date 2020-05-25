from moviepy.editor import VideoFileClip, AudioFileClip
import moviepy.video.fx.all as vfx
from misc import random_str


def extract_audio(video_path):
    """
    :param video_path: 영상에 쓰일 하이라이트 영상 경로
    :return: 영상에서 추출된 오디오 파일 경로
    """

    # Create random file name
    audio_path = random_str() + ".wav"

    # Access video file
    video_clip = VideoFileClip(video_path)

    # Extract audio file
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path)

    return audio_path


def overwrite_audio(video_path, audio_path):
    """
    :param video_path: 영상에 쓰일 하이라이트 영상 경로
    :param audio_path: 음계가 조정된 오디오 파일 경로
    :return: 조정된 하이라이트 영상 경로
    """
    # Access video file and audio file
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    # Create random file name
    video_path = random_str() + ".mp4"

    # Adjust video speed to sync with audio file
    adjusted_video = video_clip.fx(vfx.speedx, final_duration=audio_clip.duration)

    # Overwrite video audio
    adjusted_video.audio = audio_clip
    adjusted_video.write_videofile(video_path)

    return video_path

