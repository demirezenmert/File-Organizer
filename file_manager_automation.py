#! /usr/bin/env python3 

try:
    import watchdog
except ModuleNotFoundError:
    from subprocess import call
    call('pip install watchdog',shell=True)




# Module
import os
from os import scandir, rename, getcwd
from time import sleep
from os.path import exists, join, splitext
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from shutil import move 
from time import sleep
import logging


# you can use os.rename() but doesnt support different disk drives.
# from os import rename


#Directories

srcDirectory = '/Users/mertdemirezen/Documents/Projects/FileManager'
picDir = 'Pictures'
videoDir = 'Videos'
musicDir = 'Musics'
docDir = 'Documents'
sfxDir = 'Sfx'

source = [picDir,videoDir,musicDir,docDir,sfxDir]


# supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# supported Audio types
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
# supported Document types
document_extensions = [".doc", ".docx", ".odt",".pdf", ".xls", ".xlsx", ".ppt", ".pptx","txt"]




 


class FileManager(FileSystemEventHandler):

    def __init__(self):
        self.isFoldersExist()

    def on_modified(self, event):

        with scandir(srcDirectory) as entries :
            for entry in entries:
                fileName = entry.name
                
                #Checking is image?
                self.checkImageFiles(fileName)
                self.checkAudioFiles(entry,fileName)
                self.checkVideoFiles(fileName)
                self.checkDocumentFiles(entry,fileName)



    def checkAudioFiles(self, entry, name):  
        for audio_extension in audio_extensions:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                if entry.stat().st_size < 10_000_000 or "SFX" in name:  # ? 10Megabytes
                    dest = sfxDir
                else:
                    dest = musicDir
                self.moveFile(dest,name)
                sleep(0.2)
                logging.info(f"Moved audio file: {name}")

    def checkVideoFiles(self, name):  
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                self.moveFile(videoDir,name)
                sleep(0.2)
                logging.info(f"Moved video file: {name}")
    

    def checkImageFiles(self, fileName):
        for image_ext in image_extensions:
            if fileName.endswith(image_ext) or fileName.endswith(image_ext.upper()):
                self.moveFile(picDir, fileName)
                logging.info(f"Moved image file: {fileName}")
                sleep(0.2)
    
    
    
    def checkDocumentFiles(self, entry, name):  # * Checks all Document Files
        for documents_extension in document_extensions:
            if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
                self.moveFile(docDir,name)
                logging.info(f"Moved document file: {name}")
                sleep(0.2)




    def isFoldersExist(self):
        isPicDir = os.path.isdir(picDir)
        for dir in source:
            if not os.path.isdir(dir):
                os.mkdir(dir)
       
    
    
    def moveFile(self, dest, fileName):
        
        if exists(f'{dest}/{fileName}'):
            uniqueFileName = self.makeUnique(dest, fileName=fileName)
            rename(fileName, uniqueFileName)

        if not exists(f'{dest}/{fileName}') :
            move(fileName, dest)

    def makeUnique(self, dest, fileName):
        #seperating name and extention from file name
        name, extention = splitext(fileName)
        fileCounter = 1
        
        #if file exists in destination folder, adds number to the end of the file name
        while exists(f'{dest}/{fileName}'):
            
            fileName = f'{name}({str(fileCounter)}){extention}'
            fileCounter += 1
        return fileName



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = getcwd()
    event_handler = FileManager()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()