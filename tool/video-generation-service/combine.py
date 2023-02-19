"""
    Combine an audio and a video file by replacing the video file's audio track
    Note: Both of the tracks will be resized to a duration of 15 seconds.
"""
from moviepy.editor import AudioFileClip, VideoFileClip, TextClip, CompositeVideoClip
from moviepy.decorators import apply_to_audio, apply_to_mask


def speedx(clip, factor=None, final_duration=15.0):
    """
        Returns a clip playing the current clip but at a speed multiplied
        by ``factor``. Instead of factor one can indicate the desired
        ``final_duration`` of the clip, and the factor will be automatically
        computed.
        The same effect is applied to the clip's audio and mask if any.
    """

    if final_duration:
        factor = 1.0 * clip.duration / final_duration

    newclip = clip.fl_time(lambda t: factor * t, apply_to=['mask', 'audio'])

    if clip.duration is not None:
        newclip = newclip.set_duration(1.0 * clip.duration / factor)

    return newclip

def get_combined_video(input_audio_file, input_video_file, output_video_file, watermark_text = None):
    audioclip = AudioFileClip(input_audio_file)
    audioclip_cut = speedx(audioclip)
    videoclip = VideoFileClip(input_video_file)
    videoclip_cut = speedx(videoclip)
    outputclip = videoclip_cut.set_audio(audioclip_cut)
    
    if watermark_text is None:
        finalclip = outputclip
    else:
        logo = (TextClip(watermark_text)
          .set_duration(outputclip.duration)
          .resize(height=50) 
          .margin(right=8, top=8, opacity=0) 
          .set_pos(("right","top"))
        )
        finalclip = CompositeVideoClip([outputclip, logo])

    finalclip.write_videofile(output_video_file)
