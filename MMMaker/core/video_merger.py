from moviepy.editor import VideoFileClip, concatenate_videoclips
from pathlib import Path


def merge_videos(file_paths):

    clip_list = [VideoFileClip(file_path) for file_path in file_paths]
    final_clip = concatenate_videoclips(clip_list)
    final_clip.write_videofile('output.mp4')
    file_path = str(Path(file_paths[0]).parent) + '/' + 'output.mp4'

    return file_path
