"""
    Apply filters to videos provided
"""
import cv2
from moviepy.editor import VideoFileClip
from moviepy.video import fx

from moviepy.decorators import apply_to_audio, apply_to_mask


def speedx(clip, factor = None, final_duration=15.0):
    """
    Returns a clip playing the current clip but at a speed multiplied
    by ``factor``. Instead of factor one can indicate the desired
    ``final_duration`` of the clip, and the factor will be automatically
    computed.
    The same effect is applied to the clip's audio and mask if any.
    """
    
    if final_duration:
        factor = 1.0* clip.duration / final_duration
        
    newclip = clip.fl_time(lambda t: factor * t, apply_to=['mask', 'audio'])
    
    if clip.duration is not None:
        newclip = newclip.set_duration(1.0 * clip.duration / factor)
    
    return newclip

def apply_blur(image):
    return cv2.medianBlur(image,5)

def apply_brightness(image):
    return cv2.convertScaleAbs(image, alpha=2.0, beta=0.1)



"""
    Light Blur filter
"""
def apply_blur_filter(input_filename, output_filename):
    try:
        clip = VideoFileClip(input_filename)
        new_clip = clip.fl_image(apply_blur)
        new_clip_scaled = speedx(new_clip)
        new_clip_scaled.write_videofile(output_filename)

    except Exception as e:
        print(f"Error while processing the blur filter: {e.with_traceback()}")
        return None
    

"""
    Bright filter
"""
def apply_bright_filter(input_filename, output_filename):
    try:
        clip = VideoFileClip(input_filename)
        new_clip = clip.fl_image(apply_brightness)
        new_clip_scaled = speedx(new_clip)
        new_clip_scaled.write_videofile(output_filename)

    except Exception as e:
        print(f"Error while processing the bright filter: {e.with_traceback()}")
        return None