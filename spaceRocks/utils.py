#spaceRocks/utils.py

from pygame.image import load
from pygame.math import Vector2
from pathlib import Path

def load_background_image(name, with_alpha=True):
    filename = Path(__file__).parent / Path("assets/images/"+name+".png")
    image=load(filename.resolve()) #resolve helps to make a file path absolute path

    if with_alpha:
        return image.convert_alpha() #same as convert but deals with transperrancy
    
    return image.convert() #for faster blitting

def Wrap_position(position, surface):
    x, y = position
    w, h = surface.get_size()
    return Vector2(x % w, y % h)
