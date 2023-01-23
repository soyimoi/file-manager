from fileinput import filename
import os
import sys
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import pathlib


# Source and directories that files will go to, make sure to add yours 

src = '/Your source directory here/'

img_dir = '/Your directory here/'
vid_dir = '/Your directory here/'
gif_dir = '/Your directory here/'
doc_dir = '/Your directory here/'
scr_dir = '/Your directory here/'


# Most common file extensions 

img_ext = ['.JPEG', '.JPG', '.PNG', '.HEIC','.AVIF', '.SVG', '.WEBP',
            '.jpeg','.jpg', '.png', '.heic','.avif', '.svg', '.webp']

vid_ext = ['.MOV', '.MP4', '.AVI',
            '.mov', '.mp4', '.avi']

gif_ext = ['.GIF', '.gif']

doc_ext = ['.CSV', '.DOC', '.DOCX', '.PDF', '.XLS', '.XLSX', '.PPT', '.PPTX', '.TXT', '.ODP', '.EPUB', 
            '.csv', '.doc', '.docx', '.pdf', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.odp', '.epub']


# Screenshots are saved as PNG images but I wanted to redirect them to a specific folder 
# I will gather these based on the name containing 'Screenshot' instead of the file extension as above

scr_ext = 'Screenshot'


# Retrieving the files 

with os.scandir(src) as files:
    for file in files:
        
        # Some extensions look like .xxx others like .xxxx 
        # By using the pathlib library you can get the file extension easier
        ext = pathlib.Path(file.name).suffix
        scr_img = file.name[:10]
        

        try:
            if ext in img_ext and scr_img not in scr_ext:
                shutil.move(file, img_dir)
                print('File ' + file.name + ' moved to Image Directory.')
            
            elif ext in vid_ext:
                shutil.move(file, vid_dir)
                print('File ' + file.name + ' moved to Video Directory.')
            
            elif ext in gif_ext:
                shutil.move(file, gif_dir) 
                print('File ' + file.name + ' moved to GIF Directory.')
            
            elif ext in doc_ext:
                shutil.move(file, doc_dir) 
                print('File ' + file.name + ' moved to Document Directory.')

            elif scr_img in scr_ext:
                shutil.move(file, scr_dir) 
                print('File ' + file.name + ' moved to Screenshot Directory.')
        
        except Exception as exception: 
            print('File ' + file.name + ' could not be moved.')
