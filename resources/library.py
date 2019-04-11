from IPython.display import HTML, IFrame, Audio
import warnings

def style_notebook():
    style = open("./resources/style.css", "r").read()
    return HTML(style)

def show_video_file(url,width,height):
    return HTML('<video width="900" height="600" controls autoplay><source src="resources/MapBox-Isochrone-Continuous.ogg"</video>')

def show_youtube(url, width, height):
    return IFrame(url,width,height)

def play_mp3(file):
    return Audio(file)

warnings.filterwarnings('ignore')
