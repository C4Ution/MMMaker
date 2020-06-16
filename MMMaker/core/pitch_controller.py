from .video_audio_manager import extract_audio, overwrite_audios
import random

from misc import random_str

HIGHLIGHT_LENGTH = 0.7

# 미레도레 미미미 레레레 미솔솔 미레도레 미미미 레레미레도
EXAMPLE_MUSIC = [
    {
        'pitch': -5.0,  # 미
        'length': 1,
        'is_silence': False,
    },
    {
        'pitch': -7.0,  # 레
        'length': 1,
        'is_silence': False,
    },
    {
        'pitch': -9.0,  # 도
        'length': 1,
        'is_silence': False,
    },
    {
        'pitch': -7.0,  # 레
        'length': 1,
        'is_silence': False,
    },
    {
        'pitch': 0.0,  # 공백
        'length': 1,
        'is_silence': False,
    },
    {
        'pitch': -5.0,  # 미
        'length': 1,
        'is_silence': True,
    },
    {
        'pitch': -5.0,  # 미
        'length': 1,
        'is_silence': False,
    },
    {
        'pitch': -5.0,  # 미
        'length': 1,
        'is_silence': False,
    },
    {
        'pitch': 0.0,  # 공백
        'length': 1,
        'is_silence': False,
    },
    {
        'pitch': -7.0,  # 레
        'length': 1,
        'is_silence': False,
    },
    {
        'pitch': -7.0,  # 레
        'length': 1,
        'is_silence': False,
    },
    {
        'pitch': -7.0,  # 레
        'length': 1,
        'is_silence': False,
    },
]


def adjust_sounds(highlight_paths, silence_path, music):
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
    videos = []
    audios = []

    for note in music:
        video = silence_path if note['is_silence'] else random.choice(highlight_paths)
        videos.append(video)
        wav = extract_audio(video)

    return highlight_paths


def edit_sounds(path, pitch, length):
    sr = 44100
    output_path = '{}.wav'.format(random_str())
    speed = HIGHLIGHT_LENGTH / length
    y, sr = librosa.load(path, sr=sr)
    write_wav(output_path, time_stretch(pitch_shift(y, sr, pitch), speed), sr)
    return output_path


if __name__ == '__main__':
    import librosa
    from librosa.output import write_wav
    from librosa.effects import pitch_shift, time_stretch

    sr = 44100
    y, sr = librosa.load('dog.wav', sr=sr)
    write_wav('C.wav', pitch_shift(y, sr, -9.0), sr)
    write_wav('C#.wav', pitch_shift(y, sr, -8.0), sr)
    write_wav('D.wav', pitch_shift(y, sr, -7.0), sr)
    write_wav('D#.wav', pitch_shift(y, sr, -6.0), sr)
    write_wav('E.wav', pitch_shift(y, sr, -5.0), sr)
    write_wav('F.wav', pitch_shift(y, sr, -4.0), sr)
    write_wav('F#.wav', pitch_shift(y, sr, -3.0), sr)
    write_wav('G.wav', pitch_shift(y, sr, -2.0), sr)
    write_wav('G#.wav', pitch_shift(y, sr, -1.0), sr)
    write_wav('A.wav', pitch_shift(y, sr, 0.0), sr)
    write_wav('A#.wav', pitch_shift(y, sr, 1.0), sr)
    write_wav('B.wav', pitch_shift(y, sr, 2.0), sr)

    write_wav('dog_length.wav', time_stretch(y, 2), sr=sr)
