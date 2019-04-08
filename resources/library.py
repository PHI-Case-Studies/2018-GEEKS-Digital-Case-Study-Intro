from IPython.display import HTML, IFrame
from ipywidgets import Video
import warnings

def style_notebook():
    style = open("./resources/style.css", "r").read()
    return HTML(style)

def show_video_file(url,width,height):
    return HTML('<video width="900" height="600" controls autoplay><source src="resources/MapBox-Isochrone-Continuous.ogg"</video>')

def show_youtube(url, width, height):
    return IFrame(url,width,height)

def play_mp3(file):
    return HTML('<audio src="'+file+'" controls><p>If you are reading this, it is because your browser does not support the audio element</p></audio>')

warnings.filterwarnings('ignore')