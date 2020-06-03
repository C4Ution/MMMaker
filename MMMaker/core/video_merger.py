from moviepy.editor import VideoFileClip, concatenate_videoclips
from misc import get_random_name


def merge_videos(file_paths):

    clip_list = [VideoFileClip(file_path) for file_path in file_paths]
    final_clip = concatenate_videoclips(clip_list)
    file_path = get_random_name('mp4')
    final_clip.write_videofile(file_path, codec='libx264', audio_codec='aac')

    return file_path
