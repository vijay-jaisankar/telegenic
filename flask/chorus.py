from pychorus import find_and_output_chorus
"""
  Generate chorus of a song using the `pychorus` module
"""

ALLOWED_EXTENSIONS = set(['wav', 'mp4'])


def allowed_file(filename):
  return '.' in filename and \
         filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_chorus(input_filename, output_filename):
  try:
    find_and_output_chorus(input_filename, output_filename, clip_length=15)
  except Exception as e:
    print(f"Error while generating the chorus: {e}")
