
# load and display an image with Matplotlib
from matplotlib import image
from matplotlib import pyplot
from PIL import Image
import numpy as np
# load image as pixel array
# image = Image.open("C:\\Users\\Johannes\\Documents\\Studieren\\Semester 4\\Operations Research\\Schraubenzeugs_Bilder\\4003530091896\\WIN_20220507_11_56_57_Pro.jpg")
image = Image.open("C:\\Users\\Johannes\\Documents\\Studieren\\Semester 4\\Operations Research\\Schraubenzeugs_Bilder\\4003530166327\\WIN_20220507_12_15_41_Pro.jpg")
image = np.array(image.convert('L'))
# summarize shape of the pixel array
print(image.dtype)
print(image.shape)
# display the array of pixels as an image
# pyplot.imshow(image)
# pyplot.show()

# print(image)
for i, row in enumerate(image):
    if i % 10 == 0:
        print(i)
    for j, column in enumerate(row):
        if column > 128:
            image[i][j] = 0
        else:
            image[i][j] = 255

pyplot.imshow(image)
pyplot.show()

