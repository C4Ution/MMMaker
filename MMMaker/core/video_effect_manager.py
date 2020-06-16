import random
from pathlib import Path

import moviepy.video.fx.all as vfx
from moviepy.editor import VideoFileClip
from misc import WORKING_DIR, get_random_name


def _stay(video):
    file_path = get_random_name('mp4')
    video.write_videofile(file_path, codec='libx264', audio_codec='aac')
    return file_path


def _flip_x(video):
    out = video.fx(vfx.mirror_x)
    file_path = get_random_name('mp4')
    out.write_videofile(file_path, codec='libx264', audio_codec='aac')
    return file_path


def _flip_y(video):
    out = video.fx(vfx.mirror_y)
    file_path = get_random_name('mp4')
    out.write_videofile(file_path, codec='libx264', audio_codec='aac')
    return file_path


def _black_white(video):
    out = video.fx(vfx.blackwhite)
    file_path = get_random_name('mp4')
    out.write_videofile(file_path)
    return file_path


def _colorx(video):
    out = video.fx(vfx.colorx, factor=2)
    file_path = get_random_name('mp4')
    out.write_videofile(file_path, codec='libx264', audio_codec='aac')
    return file_path


def _mask_color(video):
    out = video.fx(vfx.mask_color, color=[255, 0, 0], thr=100, s=5)
    # out = video.on_color(color=(255, 255, 0))
    file_path = get_random_name('mp4')
    out.write_videofile(file_path, codec='libx264', audio_codec='aac')
    return file_path


def _rotate_90(video):
    out = video.fx(vfx.rotate, angle=90)
    file_path = get_random_name('mp4')
    out.write_videofile(file_path, codec='libx264', audio_codec='aac')
    return file_path


def _rotate_270(video):
    out = video.fx(vfx.rotate, angle=270)
    file_path = get_random_name('mp4')
    out.write_videofile(file_path, codec='libx264', audio_codec='aac')
    return file_path


def _invert_colors(video):
    out = video.fx(vfx.invert_colors)
    file_path = get_random_name('mp4')
    out.write_videofile(file_path, codec='libx264', audio_codec='aac')
    return file_path

def _painting(video):
    out = video.fx(vfx.painting, saturation = 1.6, black = 0.006)
    file_path = get_random_name('mp4')
    out.write_videofile(file_path, codec='libx264', audio_codec='aac')
    return file_path


def apply_effects(file_paths):
    effects = [
        _stay, _flip_x, _flip_y, _black_white, _colorx, _mask_color, _rotate_90, _rotate_270, _invert_colors, _painting
    ]

    new_file_paths = []

    for file_path in file_paths:
        effects_num = random.randint(0, len(effects)-1)
        new_file_paths.append(effects[effects_num](video=VideoFileClip(file_path)))

    return new_file_paths
