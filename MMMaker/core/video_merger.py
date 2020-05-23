from moviepy.editor import VideoFileClip, concatenate_videoclips
from pathlib import Path


def merge_videos(file_paths):

    f = open('mylist.txt', 'w')
    for file_path in file_paths:
        f.write('file \'{}\' \n'.format(file_path))
    f.close()

    subprocess.run(['ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.mp4'], shell=True, check=True)

    os.remove('mylist.txt')
    file_path = Path(file_paths[0]).parent

    return file_path

