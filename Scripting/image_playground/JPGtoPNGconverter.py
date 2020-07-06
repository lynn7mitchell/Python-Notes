import sys
import os
from PIL import Image

folder_name = sys.argv[1]
folder_path = os.scandir(f"./{folder_name}")
new_folder_name = sys.argv[2]
new_path = os.path.join(os.getcwd(), new_folder_name)

if(os.path.isdir(f"./{new_folder_name}")):
    print('Sorry that folder already exists')
else:
    os.mkdir(new_path)
    for item in folder_path:
        new_file = os.path.splitext(item.name)[0]
        img = Image.open(item.path)
        print(new_file)
        img.save(f'{new_path}/{new_file}.png', 'png')
       
        



# SOLUTION

# https://github.com/aneagoie/pokedex/blob/master/JPGtoPNGconverter.py

# import sys
# import os
# from PIL import Image

# path = sys.argv[1]
# directory = sys.argv[2]

# if not os.path.exists(directory):
#     os.makedirs(directory)

# for filename in os.listdir(path):
#   clean_name = os.path.splitext(filename)[0]
#   img = Image.open(f'{path}{filename}')
#   #added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
#   img.save(f'{directory}/{clean_name}.png', 'png')
#   print('all done!')