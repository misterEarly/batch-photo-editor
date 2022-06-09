import PIL

import os

from PIL import Image


path = r"C:\Users\lofru\Private Cloud\Pfadi\PfadiAfi\AL\Website\Fotos\01_Uploaded\22\goldi pfila"

name = "Goldenberg_PfiLa"

os.listdir(path)

i = 10000

for file in os.listdir(path):
    # TODO add iteration variable

    path_img = os.path.join(path, file)

    try:
        img = Image.open(path_img)

    except:
        print("couldnt open file %s" % path_img)
        continue
        # TODO raise exception

    new_name = os.path.join(
        targetpath, name + str(i)[1:] + file[-4:]
    )  # cut off the first three characters

    img.save(new_name)
    img.close()

    i += 1
