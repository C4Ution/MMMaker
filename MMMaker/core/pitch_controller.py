from core.music_manager import get_random_music
from core.video_audio_manager import extract_audio, overwrite_audio
import random

from misc import random_str, get_random_name
import librosa
from librosa.output import write_wav
from librosa.effects import pitch_shift, time_stretch

HIGHLIGHT_LENGTH = 0.2


def adjust_sounds(highlight_paths, silence_paths, music):
    """
    :param highlight_paths: 하이라이트 영상 경로 리스트
    :param silence_path: 빈 소리 영상 경로
    :param music:
        example)
            [
                {
                    'pitch': 4.5,
                    'length': 0.7,
                    'is_silence': False,
                },
                ...
            ]
    :return: 음계가 조정된 하이라이트 영상 경로 리스트
    도 -9
    도# -8
    레 -7
    레# -6
    미 -5
    파 -4
    파# -3
    솔 -2
    솔# -1
    라 0
    라# 1
    시 2
    """
    ret = []
    for note in music:
        video = random.choice(silence_paths) if note['is_silence'] else random.choice(highlight_paths)
        wav = edit_sounds(extract_audio(video), note['pitch'], note['length'])
        ret.append(overwrite_audio(video, wav))

    return ret


def edit_sounds(path, pitch, length):
    sr = 44100
    output_path = get_random_name('wav')
    speed = HIGHLIGHT_LENGTH / length
    y, sr = librosa.load(path, sr=sr)
    write_wav(output_path, time_stretch(pitch_shift(y, sr, pitch), speed), sr)
    return output_path


if __name__ == '__main__':
    adjust_sounds(['MaxHighlight.mp4'], ['MinHighlight.mp4'], get_random_music())
    pass
    # import librosa
    # from librosa.output import write_wav
    # from librosa.effects import pitch_shift, time_stretch
    #
    # sr = 44100
    # y, sr = librosa.load('dog.wav', sr=sr)
    # write_wav('C.wav', pitch_shift(y, sr, -9.0), sr)
    # write_wav('C#.wav', pitch_shift(y, sr, -8.0), sr)
    # write_wav('D.wav', pitch_shift(y, sr, -7.0), sr)
    # write_wav('D#.wav', pitch_shift(y, sr, -6.0), sr)
    # write_wav('E.wav', pitch_shift(y, sr, -5.0), sr)
    # write_wav('F.wav', pitch_shift(y, sr, -4.0), sr)
    # write_wav('F#.wav', pitch_shift(y, sr, -3.0), sr)
    # write_wav('G.wav', pitch_shift(y, sr, -2.0), sr)
    # write_wav('G#.wav', pitch_shift(y, sr, -1.0), sr)
    # write_wav('A.wav', pitch_shift(y, sr, 0.0), sr)
    # write_wav('A#.wav', pitch_shift(y, sr, 1.0), sr)
    # write_wav('B.wav', pitch_shift(y, sr, 2.0), sr)
    #
    # write_wav('dog_length.wav', time_stretch(y, 2), sr=sr)
