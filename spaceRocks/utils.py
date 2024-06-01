#spaceRocks/utils.py

from pygame.image import load
from pathlib import Path

def load_background_image(name, with_alpha=True):
    filename = Path(__file__).parent / Path("assets/images/"+name+".png")
    image=load(filename.resolve()) #resolve helps to make a file path absolute path

    if with_alpha:
        return image.convert_alpha() #same as convert but deals with transperrancy
    
    return image.convert() #for faster blitting
