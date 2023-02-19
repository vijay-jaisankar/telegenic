
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime
import os

# Application-specific imports
from chorus import save_chorus, allowed_file
from filters import apply_colour_change_filter, apply_scroll_filter, apply_colourx_filter
from beeceptor import get_url_from_beeceptor
from generate import get_combined_video

app = Flask(__name__)


@app.route('/')
def index():
  url = get_url_from_beeceptor()
  # url = None
  return render_template("index.html", bg=url)

"""
  Chorus generation
"""


@app.route("/audio", methods=["GET", "POST"])
def audio():
  if request.method == "POST":
    file = request.files["file"]
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      salted_filename = f'{filename.split(".")[0]}_{str(datetime.now())}.wav'
      saved_input = os.path.join("input", salted_filename)
      file.save(saved_input)

      saved_output = os.path.join("output", salted_filename)
      save_chorus(saved_input, saved_output)

      return send_from_directory("output", salted_filename)

  return render_template("audio.html")


"""
  Video Filters
"""


@app.route("/video", methods=["GET", "POST"])
def video():
  if request.method == "POST":
    file = request.files["file"]
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      salted_filename = f'{filename.split(".")[0]}_{str(datetime.now())}.mp4'
      saved_input = os.path.join("input", salted_filename)
      file.save(saved_input)

      saved_output = os.path.join("output", salted_filename)

      option = request.form['options']
      if str(option) == "colour":
        apply_colourx_filter(saved_input, saved_output)

      else:
        apply_scroll_filter(saved_input, saved_output)

      return send_from_directory("output", salted_filename)

  return render_template("video.html")


"""
  Generate combined video
"""


@app.route("/generate", methods=["GET", "POST"])
def generate():
  if request.method == "POST":
    files = request.files.getlist("file")
    audiofile = None
    videofile = None
    for f in files:
      if "wav" in f.filename:
        audiofile = f
      if "mp4" in f.filename:
        videofile = f

    if audiofile is not None and videofile is not None:
      audio_filename = secure_filename(audiofile.filename)
      audio_salted_filename = f'{audio_filename.split(".")[0]}_{str(datetime.now())}.wav'
      audio_saved_input = os.path.join("input", audio_salted_filename)
      audiofile.save(audio_saved_input)

      video_filename = secure_filename(videofile.filename)
      video_salted_filename = f'{video_filename.split(".")[0]}_{str(datetime.now())}.mp4'
      video_saved_input = os.path.join("input", video_salted_filename)
      videofile.save(video_saved_input)

      saved_output = os.path.join("output", video_salted_filename)
      print(audio_saved_input, video_saved_input, saved_output)
      get_combined_video(audio_saved_input, video_saved_input, saved_output)

      return send_from_directory("output", video_salted_filename)

  return render_template("generate.html")


app.run(host='0.0.0.0', port=81)
