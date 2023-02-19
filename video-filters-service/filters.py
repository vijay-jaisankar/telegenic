"""
    Apply filters to videos provided
"""
import cv2
from moviepy.editor import VideoFileClip

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
        new_clip.write_videofile(output_filename)

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
        new_clip.write_videofile(output_filename)

    except Exception as e:
        print(f"Error while processing the bright filter: {e.with_traceback()}")
        return None