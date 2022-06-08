import PIL

import os

from PIL import Image


path = r"C:\Users\lofru\Private Cloud\Pfadi\PfadiAfi\AL\Website\Fotos\01_Uploaded\22\goldi pfila"

name = "Goldenberg_PfiLa"

os.listdir(path)

for file in os.listdir(path):
    # TODO add iteration variable

    path_img = os.path.join(path, file)

    try:
        img = Image.open(path_img)

    except:
        print("couldnt open file %s" % path_img)
        continue
        # TODO raise exception

    new_name = os.path.join(path, name + file[3:])  # cut off the first three characters

    img.save(new_name)
    img.close()
