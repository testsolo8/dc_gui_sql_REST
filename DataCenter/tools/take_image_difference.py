from PIL import Image


def percent_image_difference(im1, im2):
    i1 = Image.open(im1)
    i2 = Image.open(im2)
    pairs = zip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1 - p2) for p1, p2 in pairs)
    else:
        dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))
    ncomponents = i1.size[0] * i1.size[1] * 3
    # print("Difference (percentage):", (dif / 255.0 * 100) / ncomponents)
    return (dif / 255.0 * 100) / ncomponents


def get_difference_between_checkbox_image(image1, image2):
    image_a = Image.open(image1).getdata()
    image_b = Image.open(image2).getdata()
    difference = 0
    for pixel_a, pixel_b in zip(image_a, image_b):
        if pixel_a != pixel_b:
            difference += 1
    return difference
