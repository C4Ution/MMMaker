from core.music_manager import get_random_music
from core.pitch_controller import adjust_sounds
from core.video_merger import merge_videos
from core.highlight_extractor import extract_highlights
from core.video_effect_manager import apply_effects


def run():

    print(extract_highlights(['/Users/myeongsegyo/Workspace/MMMaker/MMMaker/core/source4.mp4']))
