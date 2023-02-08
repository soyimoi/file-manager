from fileinput import filename
import os
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

img_ext = ['.JPEG', '.JPG', '.PNG', '.HEIC','.AVIF', '.SVG', '.WEBP']
vid_ext = ['.MOV', '.MP4', '.AVI']
gif_ext = ['.GIF']
doc_ext = ['.CSV', '.DOC', '.DOCX', '.PDF', '.XLS', '.XLSX', '.PPT', '.PPTX', '.TXT', '.ODP', '.EPUB']


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
            if ext.lower() in img_ext or ext.upper() in img_ext and scr_img not in scr_ext:
                shutil.move(file, img_dir)
                print('File ' + file.name + ' moved to Image Directory.')
            
            elif ext.lower() in vid_ext or ext.upper() in vid_ext:
                shutil.move(file, vid_dir)
                print('File ' + file.name + ' moved to Video Directory.')
            
            elif ext.lower() in gif_ext or ext.upper() in gif_ext:
                shutil.move(file, gif_dir) 
                print('File ' + file.name + ' moved to GIF Directory.')
            
            elif ext.lower() in doc_ext or ext.upper() in doc_ext:
                shutil.move(file, doc_dir) 
                print('File ' + file.name + ' moved to Document Directory.')

            elif scr_img in scr_ext:
                shutil.move(file, scr_dir) 
                print('File ' + file.name + ' moved to Screenshot Directory.')
        
        except Exception as exception: 
            print('File ' + file.name + ' could not be moved.')
            
            
            
            
            
