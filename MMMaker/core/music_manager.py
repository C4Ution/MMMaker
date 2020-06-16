import random

# 떳다떳다 비행기
# 미레도레 미미미 레레레 미솔솔 미레도레 미미미 레레미레도
selected_music = ''

AIRPLANE_MUSIC = [
    {
        'pitch': -5.0,  # 미
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -7.0,  # 레
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -9.0,  # 도
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -7.0,  # 레
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -5.0,  # 미
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -5.0,  # 미
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -5.0,  # 미
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': 0.0,  # 공백
        'length': 0.15,
        'is_silence': True,
    },
    {
        'pitch': -7.0,  # 레
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -7.0,  # 레
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -7.0,  # 레
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': 0.0,  # 공백
        'length': 0.15,
        'is_silence': True,
    },
    {
        'pitch': -5.0,  # 미
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -2.0,  # 솔
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -2.0,  # 솔
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': 0.0,  # 공백
        'length': 0.15,
        'is_silence': True,
    },
    {
        'pitch': -5.0,  # 미
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -7.0,  # 레
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -9.0,  # 도
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -7.0,  # 레
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -5.0,  # 미
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -5.0,  # 미
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -5.0,  # 미
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': 0.0,  # 공백
        'length': 0.15,
        'is_silence': True,
    },
    {
        'pitch': -7.0,  # 레
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -7.0,  # 레
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -5.0,  # 미
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -7.0,  # 레
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -9.0,  # 도
        'length': 0.1,
        'is_silence': False,
    },
]

# 아기상어
# 레미 솔솔 솔솔솔솔솔 레미솔 솔솔솔솔솔 레미솔 솔솔솔솔솔 솔솔 파파
BABY_SHARK_MUSIC = [
    {
        'pitch': 0.0,  # 공백
        'length': 0.4,
        'is_silence': True,
    },
    {
        'pitch': 0.0,  # 공백
        'length': 0.2,
        'is_silence': True,
    },
    {
        'pitch': 0.0,  # 공백
        'length': 0.4,
        'is_silence': True,
    },
    {
        'pitch': 0.0,  # 공백
        'length': 0.2,
        'is_silence': True,
    },
    {
        'pitch': 0.0,  # 공백
        'length': 0.2,
        'is_silence': True,
    },
    {
        'pitch': 0.0,  # 공백
        'length': 0.1,
        'is_silence': True,
    },
    {
        'pitch': 0.0,  # 공백
        'length': 0.2,
        'is_silence': True,
    },
    {
        'pitch': 0.0,  # 공백
        'length': 0.2,
        'is_silence': True,
    },
    {
        'pitch': 0.0,  # 공백
        'length': 0.25,
        'is_silence': True,
    },

    {
        'pitch': -7.0,  # 레
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -5.0,  # 미
        'length': 0.1,
        'is_silence': False,
    },


    {
        'pitch': -2.0,  # 솔
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -2.0,  # 솔
        'length': 0.1,
        'is_silence': False,
    },

    {
        'pitch': -2.0,  # 솔
        'length': 0.05,
        'is_silence': False,
    },
    {
        'pitch': -2.0,  # 솔
        'length': 0.05,
        'is_silence': False,
    },
    {
        'pitch': -2.0,  # 솔
        'length': 0.05,
        'is_silence': False,
    },
    {
        'pitch': -2.0,  # 솔
        'length': 0.05,
        'is_silence': False,
    },

    {
        'pitch': -7.0,  # 레
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -5.0,  # 미
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -2.0,  # 솔
        'length': 0.1,
        'is_silence': False,
    },

    {
        'pitch': -2.0,  # 솔
        'length': 0.05,
        'is_silence': False,
    },
    {
        'pitch': -2.0,  # 솔
        'length': 0.05,
        'is_silence': False,
    },
    {
        'pitch': -2.0,  # 솔
        'length': 0.05,
        'is_silence': False,
    },
    {
        'pitch': -2.0,  # 솔
        'length': 0.05,
        'is_silence': False,
    },

    {
        'pitch': -7.0,  # 레
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -5.0,  # 미
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -2.0,  # 솔
        'length': 0.1,
        'is_silence': False,
    },

    {
        'pitch': -2.0,  # 솔
        'length': 0.05,
        'is_silence': False,
    },
    {
        'pitch': -2.0,  # 솔
        'length': 0.05,
        'is_silence': False,
    },
    {
        'pitch': -2.0,  # 솔
        'length': 0.05,
        'is_silence': False,
    },
    {
        'pitch': -2.0,  # 솔
        'length': 0.05,
        'is_silence': False,
    },

    {
        'pitch': -2.0,  # 솔
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -2.0,  # 솔
        'length': 0.05,
        'is_silence': False,
    },

    {
        'pitch': -4.0,  # 파
        'length': 0.1,
        'is_silence': False,
    },
    {
        'pitch': -4.0,  # 파
        'length': 0.05,
        'is_silence': False,
    },
]


def get_random_music():
    musics = [
        AIRPLANE_MUSIC, BABY_SHARK_MUSIC,
    ]

    music_num = random.randint(0, len(musics)-1)

    global selected_music

    if music_num == 0:
        selected_music = 'AIRPLANE_MUSIC'
    elif music_num == 1:
        selected_music = 'BABY_SHARK_MUSIC'

    return musics[music_num]


def get_selected_music():

    return selected_music



