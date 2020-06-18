import random
from pathlib import Path
from vidpy import config, Clip, Composition

import moviepy.video.fx.all as vfx
from moviepy.editor import VideoFileClip
from misc import WORKING_DIR, get_random_name

config.MELT_BINARY = '/usr/bin/melt'


def _stay(file_path):
    video = VideoFileClip(file_path)
    file_path = get_random_name('mp4')
    video.write_videofile(file_path, codec='libx264', audio_codec='aac')
    return file_path


def _flip_x(file_path):
    video = VideoFileClip(file_path)
    out = video.fx(vfx.mirror_x)
    file_path = get_random_name('mp4')
    out.write_videofile(file_path, codec='libx264', audio_codec='aac')
    return file_path


def _flip_y(file_path):
    video = VideoFileClip(file_path)
    out = video.fx(vfx.mirror_y)
    file_path = get_random_name('mp4')
    out.write_videofile(file_path, codec='libx264', audio_codec='aac')
    return file_path


def _black_white(file_path):
    video = VideoFileClip(file_path)
    out = video.fx(vfx.blackwhite)
    file_path = get_random_name('mp4')
    out.write_videofile(file_path)
    return file_path


def _colorx(file_path):
    video = VideoFileClip(file_path)
    out = video.fx(vfx.colorx, factor=2)
    file_path = get_random_name('mp4')
    out.write_videofile(file_path, codec='libx264', audio_codec='aac')
    return file_path


def _mask_color(file_path):
    video = VideoFileClip(file_path)
    out = video.fx(vfx.mask_color, color=[255, 0, 0], thr=100, s=5)
    # out = video.on_color(color=(255, 255, 0))
    file_path = get_random_name('mp4')
    out.write_videofile(file_path, codec='libx264', audio_codec='aac')
    return file_path


def _rotate_90(file_path):
    video = VideoFileClip(file_path)
    out = video.fx(vfx.rotate, angle=90)
    file_path = get_random_name('mp4')
    out.write_videofile(file_path, codec='libx264', audio_codec='aac')
    return file_path


def _rotate_270(file_path):
    video = VideoFileClip(file_path)
    out = video.fx(vfx.rotate, angle=270)
    file_path = get_random_name('mp4')
    out.write_videofile(file_path, codec='libx264', audio_codec='aac')
    return file_path


def _invert_colors(file_path):
    video = VideoFileClip(file_path)
    out = video.fx(vfx.invert_colors)
    file_path = get_random_name('mp4')
    out.write_videofile(file_path, codec='libx264', audio_codec='aac')
    return file_path


def _painting(file_path):
    video = VideoFileClip(file_path)
    out = video.fx(vfx.painting, saturation = 1.6, black = 0.006)
    file_path = get_random_name('mp4')
    out.write_videofile(file_path, codec='libx264', audio_codec='aac')
    return file_path


def _video_grid(video):
    canvas_width = 1280
    canvas_height = 720
    vid_width = canvas_width/3
    vid_height = (vid_width/canvas_width) * canvas_height

    x = 0
    y = 0

    while y < canvas_height:


def _video_zoompan(file_path):
    video = Clip(file_path)
    video.zoompan([0, 0, '100%', '100%'], [100, 100, '50%', '50%'], start=0, end=5)
    file_path = get_random_name('mp4')
    video.save(file_path)
    return file_path


def _video_spin(file_path):
    video = Clip(file_path)
    video.spin(50)
    file_path = get_random_name('mp4')
    video.save(file_path)
    return file_path


def _video_spin_zoompan(file_path):
    video = Clip(file_path)
    video.spin(50)
    video.zoompan([0, 0, '100%', '100%'], [100, 100, '50%', '50%'], start=0, end=5)
    file_path = get_random_name('mp4')
    video.save(file_path)
    return file_path


def _video_mirror(file_path):
    video = Clip(file_path)
    video.mirror()
    file_path = get_random_name('mp4')
    video.save(file_path)
    return file_path


def apply_effects(file_paths):
    effects = [
        _stay, _flip_x, _flip_y, _black_white, _colorx, _mask_color, _rotate_90, _rotate_270, _invert_colors, _painting
        _video_zoompan, _video_spin, _video_spin_zoompan, _video_mirror
    ]

    new_file_paths = []

    for file_path in file_paths:
        effects_num = random.randint(0, len(effects)-1)
        new_file_paths.append(effects[effects_num](file_path))

    return new_file_paths
