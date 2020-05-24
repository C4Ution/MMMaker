import pitch
from pydub import AudioSegment
from pydub.playback import play


def adjust_sounds(highlight_paths, silence_path, music):

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


"""

ffmpeg -i dog_barking_10sec.mp4 dog_barking.wav
"""
#
sound = AudioSegment.from_file('dog.wav', format="wav")

do = sound._spawn(sound.raw_data, overrides={'frame_rate': 26100})
do_shop = sound._spawn(sound.raw_data, overrides={'frame_rate': 27700})
rae = sound._spawn(sound.raw_data, overrides={'frame_rate': 29300})
rae_shop = sound._spawn(sound.raw_data, overrides={'frame_rate': 31100})
mi = sound._spawn(sound.raw_data, overrides={'frame_rate': 32900})
pa = sound._spawn(sound.raw_data, overrides={'frame_rate': 34900})
pa_shop = sound._spawn(sound.raw_data, overrides={'frame_rate': 36900})
sol = sound._spawn(sound.raw_data, overrides={'frame_rate': 39100})
sol_shop = sound._spawn(sound.raw_data, overrides={'frame_rate': 41500})
la = sound._spawn(sound.raw_data, overrides={'frame_rate': 44000})
la_shop = sound._spawn(sound.raw_data, overrides={'frame_rate': 46600})
si = sound._spawn(sound.raw_data, overrides={'frame_rate': 49300})
#
#
# play(sound._spawn(sound.raw_data, overrides={'frame_rate': 16000}).set_frame_rate(49300))
# play(sound._spawn(sound.raw_data, overrides={'frame_rate': 16000}))
# play(sound)


# 미레도레미미미 레레레 미솔솔 미레도레 미미미 레레미레도
play(mi)
play(rae)
play(do)
play(rae)
play(mi)
play(mi)
play(mi)
play(rae)
play(rae)
play(rae)
play(mi)
play(sol)
play(sol)

import librosa

sr = 44100
y, sr = librosa.load('dog.wav', sr=sr)
y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=4.0, bins_per_octave=24)
librosa.output.write_wav('dog_length.wav', librosa.effects.time_stretch(y_shifted, 2), sr=sr)
librosa.output.write_wav('dog2.wav', y_shifted, sr=sr)
