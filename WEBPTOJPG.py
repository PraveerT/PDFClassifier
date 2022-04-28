import os
import glob
from PIL import Image
path="C:\\Users\\prav\\Documents\\ST FINAL\\S5\\photo_2\\"
for filename in glob.glob(os.path.join(path,'*.webp')):
    print (filename)
    im=Image.open(filename).convert("RGB")
    im.save(filename+".jpg","jpeg")

