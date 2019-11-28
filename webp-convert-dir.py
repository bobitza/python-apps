# --cwebp_compressor.py--  COMMAND: python3 webp-convert-dir.py DIR 70

# cmd> python cwebp_compressor.py folder-name 80

import sys
from subprocess import call
import os

#folder-name
path = sys.argv[1]
#quality of produced .webp images [0-100]
quality = sys.argv[2]

if int(quality) < 0 or int(quality) > 100:
    print("image quality out of range[0-100] ;/:/")
    sys.exit(0)

img_list = []
#for img_name in glob(path+'/*', recursive=True):
filearrays = { '.jpeg':[],'.svg':[],'.jpg':[],'.png':[] }
for root,dirs,files in os.walk(path+'/'):
    for file in files:
        filename, fileext = os.path.splitext(file)

    # one can use more image types(bmp,tiff,gif)
        if fileext in filearrays:
        # extract images name(image_name.[jpg|png]) from the full path
            img_list.append(os.path.join(root, file))


#print(img_list)   # for debug
#sys.exit(0)
#os.chdir(r'images/')
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
for img_name in img_list:
    cmd=['cwebp \"'+cwd+'/'+img_name+'\" -q '+quality+' -o \"'+cwd+'/'+(img_name.split('.')[0])+'.webp\"']
    # running the above command
    call(cmd, shell=True)
