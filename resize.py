import PIL

import os

from PIL import Image


path = r"C:\Users\Lovis\OneDrive - ZHAW\Pfadi\PfadiAfi\AL\Website\Fotos\01_Uploaded\21 Sambucus Aktivitaeten"
max_edge_length = 1000  # define length of longer side in resized image

os.listdir(path)

for file in os.listdir(path):

    path_img = os.path.join(path, file)

    try:
        img = Image.open(path_img)

    except:
        print("couldnt open file %s" % path_img)
        continue
        # todo raise exception

    # check if image is landscape or portrait

    width = img.width
    height = img.height

    # todo add check if image is actually larger than goal size
    ratio = width / height

    if (
        ratio < 1
    ):  # if ratio is less than 1, it is portrait. if its portrait, the height has to be equal to max_edge_length

        edge_ratio = height / max_edge_length
        new_height = max_edge_length
        new_width = width / edge_ratio

    elif (
        ratio > 1
    ):  # if ratio is greater than 1, it is landscape. if its landscape, the width has to be equal to max_edge_length

        edge_ratio = width / max_edge_length
        new_width = max_edge_length
        new_height = height / edge_ratio

    elif ratio == 1:  # catch exact squares
        new_width = max_edge_length
        new_height = max_edge_length

    else:
        print("couldnt resize for some reason")
        continue
        # todo add better error message
        # todo raise exception

    new_width = round(new_width)
    new_height = round(new_height)

    img = img.resize((new_width, new_height))
    img.save(path_img)
    img.close()
