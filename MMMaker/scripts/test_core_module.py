from core.music_manager import get_random_music
from core.pitch_controller import adjust_sounds
from core.video_merger import merge_videos
from core.highlight_extractor import extract_highlights
from core.video_effect_manager import apply_effects


def run():
    max_highlights, min_highlights = extract_highlights(['/home/simhongsub/dev/workspace/MMMaker/MMMaker/core/SourceVideo.mp4'])
    videos = adjust_sounds(max_highlights, min_highlights, get_random_music())
    videos = apply_effects(videos)
    print(merge_videos(videos))
