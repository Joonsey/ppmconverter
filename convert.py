from PIL import Image
from math import floor
import os


SOURCE_IMAGE_PATH = "images/"
DEST_IMAGE_PATH = "converted_images/"
# i hardcoded the images array because it is faster than using the function.
# and i produce the images in a way that's easy for them to be formated in this way.
images = ["weights-{:02d}".format(x) for x in range(100)]


# this function will find all images of type .ppm in given dir
def find_images(src_dir:str) -> list:
    files = []
    for file in os.listdir(src_dir):
        if file.endswith('.ppm'):
            files.append(file)

    return files



# takes array of file names
# this can be procedurally generated as above or done through
def convert(images:list, verbose=True):
    N = len(images)
    index = 0
    for i in images:
        index+=1
        try:
            im = Image.open(SOURCE_IMAGE_PATH+i+".ppm")
            try:
                im.save(DEST_IMAGE_PATH+i+".png")
                if verbose:
                    print(f"\r--------{floor((index/N)*100)}%--------", end="")
                    continue
            except: 
                print('failed to save ' + i)
        except:
            print("failed converting: "+i)


if __name__ == "__main__":
    convert(images)
