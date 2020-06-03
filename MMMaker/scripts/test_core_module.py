from core.pitch_controller import adjust_sounds, EXAMPLE_MUSIC
from core.video_merger import merge_videos
from core.highlight_extractor import extract_highlights
from core.video_effect_manager import apply_effects


def run():
    max_highlights, min_highlights = extract_highlights(['/Users/myeongsegyo/Workspace/MMMaker/MMMaker/core/SourceVideo.mp4'])
    videos = adjust_sounds(max_highlights, min_highlights, EXAMPLE_MUSIC)
    videos = apply_effects(videos)
    print(merge_videos(videos))
