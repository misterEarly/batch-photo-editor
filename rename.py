import PIL

import os

from PIL import Image


path = r"C:\Users\Lovis\OneDrive - ZHAW\Pfadi\PfadiAfi\AL\Website\Fotos\01_Uploaded\21 Sambucus Aktivitaeten"

name = "Sambucus_Herbst_Aktivitaeten"

os.listdir(path)

for file in os.listdir(path):

    path_img = os.path.join(path, file)

    try:
        img = Image.open(path_img)

    except:
        print("couldnt open file %s" % path_img)
        continue
        # todo raise exception

    new_name = os.path.join(path, name + file[3:])

    img.save(new_name)
    img.close()
