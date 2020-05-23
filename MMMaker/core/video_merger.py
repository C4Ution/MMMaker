from moviepy.editor import VideoFileClip, concatenate_videoclips
from pathlib import Path


def merge_videos(file_paths):

    clip_list = [VideoFileClip(file_path) for file_path in file_paths]
    final_clip = concatenate_videoclips(clip_list)
    final_clip.write_videofile('output.mp4')
    f.close()

    subprocess.run(['ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.mp4'], shell=True, check=True)

    os.remove('mylist.txt')
    file_path = Path(file_paths[0]).parent

    return file_path

