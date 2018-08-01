import cv2

#print(type(img)) # shows data type of img

#print(img) # will print raw data (in numpy.ndarray)

#s_size = []
#size = []


def shrink(img_path, factor, save = True):
    img = cv2.imread(img_path, 0) # 0 for greyscale, 1 for color, -1 for opacity
    img_name = ''
    s_size = []
    size = list(img.shape)
    count = 0

    for pixels in size:
        pixels = pixels / int(factor)
        count += 1
        if count == 2:
            h_size = int(pixels)
        else:
            w_size = int(pixels)

    resized_image = cv2.resize(img, (h_size, w_size))

    if save == True:
        img_name = "galaxy_{}.jpg".format(str(img.shape)[1: -1]).replace(', ', 'x')
        cv2.imwrite(img_name, resized_image)
        preview = input("Would you like to see the image? [Y/n]")

        if preview.lower() == 'y':
            cv2.imshow(img_name, img)
            cv2.waitKey(0) # will wait for any key press
            cv2.destroyAllWindows()

    preview = input("Would you like to see the image? [Y/n]")

    if preview.lower() == 'y':
        cv2.imshow(img_name, img)
        cv2.waitKey(0) # will wait for any key press
        cv2.destroyAllWindows()

    return resized_image


def main():
    img_path = input('Where is your image located?  ')
    factor = input('How many times smaller would you like it to be? ')
    act = input('Are you saving the shrunken image? [Y/n]')

    if act.lower() == 'y':
        save = True
    else:
        save = False

    shrink(img_path, factor, act)

    print('Enjoy your tiny pic :]')
    exit()


main()
