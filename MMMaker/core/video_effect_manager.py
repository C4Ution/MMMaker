import random
from pathlib import Path

import moviepy.video.fx.all as vfx
from moviepy.editor import VideoFileClip, concatenate_videoclips


def _stay(video, idx):
    video.write_videofile('out{}.mp4'.format(idx))


def _flip_x(video, idx):
    out = video.fx(vfx.mirror_x)
    out.write_videofile('out{}.mp4'.format(idx))


def _flip_y(video, idx):
    out = video.fx(vfx.mirror_y)
    out.write_videofile('out{}.mp4'.format(idx))


def apply_effects(file_paths):
    effects = [
        _stay, _flip_x, _flip_y,
    ]

    new_file_paths = []

    for idx, file_path in enumerate(file_paths):
        effects_num = random.randint(0, len(effects)-1)
        effects[effects_num](idx=idx, video=VideoFileClip(file_path))
        new_file_paths.append(str(Path(file_path).parent) + '/' + 'out{}.mp4'.format(idx))

    return new_file_paths
