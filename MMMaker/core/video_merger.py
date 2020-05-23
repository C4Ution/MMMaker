import subprocess
import os
def merge_videos(file_paths):

    f = open('mylist.txt', 'w')
    for file_path in file_paths:
        f.write('file \'{}\' \n'.format(file_path))
    f.close()

    :param file_paths: 합쳐야할 영상 경로 리스트
    :return: 합쳐진 영상 경로
    """
    file_path = ''
    return file_path
