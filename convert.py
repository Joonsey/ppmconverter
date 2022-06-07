from PIL import Image

SOURCE_IMAGE_PATH = "images/"
DEST_IMAGE_PATH = "converted_images/"


def convert(images):
    for i in images:
        try:
            im = Image.open(SOURCE_IMAGE_PATH+i+".ppm")
            try:
                im.save(DEST_IMAGE_PATH+i+".png")
            except: 
                print('failed to save' + i)
        except:
            print("failed converting: "+i)


images = ["weights-{:02d}".format(x) for x in range(100)]


if __name__ == "__main__":
    convert(images)
