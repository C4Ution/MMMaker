import subprocess
import os
def merge_videos(file_paths):

    f = open('mylist.txt', 'w')
    for file_path in file_paths:
        f.write('file \'{}\' \n'.format(file_path))
    f.close()

    subprocess.run(['ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.mp4'], shell=True, check=True)
    :return: 합쳐진 영상 경로
    """
    file_path = ''
    return file_path
