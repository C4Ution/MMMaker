from moviepy.editor import VideoFileClip, concatenate_videoclips
from core.video_audio_manager import add_background_audio
from misc import get_random_name


def merge_videos(file_paths):

    clip_list = [VideoFileClip(file_path) for file_path in file_paths]
    final_clip = concatenate_videoclips(clip_list)
    file_path = get_random_name('mp4')

    # Insert background audio
    final_clip.audio = add_background_audio(final_clip.audio)

    final_clip.write_videofile(file_path, codec='libx264', audio_codec='aac')

    return file_path
