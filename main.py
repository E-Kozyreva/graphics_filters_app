import classes
from threading import Thread
from PIL import Image


if __name__ == "__main__":
    img = Image.open('cat.jpg')
    spot = classes.SpotFilters(img)
    matrix = classes.MatrixFilters(img)

    t1 = Thread(target=spot.inversion)
    t2 = Thread(target=spot.grayscale)
    t3 = Thread(target=spot.blackwhite)
    t4 = Thread(target=spot.sepia)
    t5 = Thread(target=spot.brightness, args=(100,))

    t1.start()
