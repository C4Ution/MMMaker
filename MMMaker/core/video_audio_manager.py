from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
import moviepy.video.fx.all as vfx
from moviepy.audio.fx.volumex import volumex
from misc import get_random_name
from django.conf import settings


def extract_audio(video_path):
    """
    :param video_path: 영상에 쓰일 하이라이트 영상 경로
    :return: 영상에서 추출된 오디오 파일 경로
    """
    # Create random file name
    audio_path = get_random_name('wav')

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
    video_path = get_random_name('mp4')

    # Adjust video speed to sync with audio file
    adjusted_video = video_clip.fx(vfx.speedx, final_duration=audio_clip.duration)

    # Overwrite video audio
    adjusted_video.audio = audio_clip
    adjusted_video.write_videofile(video_path, codec='libx264', audio_codec='aac')

    return video_path


def add_background_audio(audio_clip):
    """
    :param audio_clip: 최종 영상 오디오 클립
    :return: 배경음 삽입된 오디오 클립
    """

    # Access audio file
    back_audio = AudioFileClip(settings.BASE_DIR + '/core/back_audios/airplanebeat.wav')

    # Extract audio file
    audio_clip = CompositeAudioClip([audio_clip.fx(volumex, 7), back_audio.fx(volumex, 1)])

    return audio_clip


# if __name__ == '__main__':
#     video_clip = VideoFileClip('back_audios/airplane.mp4')
#
#     # extract video subclip
#     sub_video = video_clip.subclip(9, 22)
#     sub_video.write_videofile('back_audios/subairplane.mp4', codec='libx264', audio_codec='aac')
#
#     video_clip = VideoFileClip('back_audios/subairplane.mp4')
#
#     new_video = video_clip.fx(vfx.speedx, final_duration=13)
#     # new_video.write_videofile('back_audios/subspeedupvideoplayback.mp4', codec='libx264', audio_codec='aac')
#
#     audio_clip = new_video.audio
#     audio_clip.write_audiofile('back_audios/airplane.wav')
#
#     video_clip = VideoFileClip('back_audios/airplanebeat.mp4')
#
#     #extract video subclip
#     sub_video = video_clip.subclip(9, 22)
#     sub_video.write_videofile('back_audios/subairplanebeat.mp4', codec='libx264', audio_codec='aac')
#
#     video_clip = VideoFileClip('back_audios/subairplanebeat.mp4')
#
#     new_video = video_clip.fx(vfx.speedx, final_duration=13)
#     #new_video.write_videofile('back_audios/subspeedupvideoplayback.mp4', codec='libx264', audio_codec='aac')
#
#     audio_clip = new_video.audio
#     audio_clip.write_audiofile('back_audios/airplanebeat.wav')

