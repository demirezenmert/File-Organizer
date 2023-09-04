#! /usr/bin/env python3 

# try:
#     from watchdog.observers import Observer
#     from watchdog.events import FileSystemEventHandler



# Module

import os
from time import sleep
from os.path import exists, join, splitext
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from shutil import move 
# you can use os.rename() but doesnt support different disk drives.
# from os import rename


#Directories

srcDirectory = '/Users/mertdemirezen/Documents/Projects/FileManager'




# supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# supported Audio types
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
# supported Document types
document_extensions = [".doc", ".docx", ".odt",".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

def makeUnique(dest, fileName):
    pass

def moveFile(dest, entry, fileName):
    if exists(f'{dest}/{fileName}'):
        makeUnique(dest, fileName=fileName)



class FileManager(FileSystemEventHandler):

    def on_modified(self, event):

        with os.scandir(srcDirectory) as entries :
            for entry in entries:
                fileName = entry.name
                
                #Checking is image?
                self.checkImageFiles(entry, fileName)

    def checkImageFiles(self, entry, fileName):
        for image_ext in image_extensions:
            if fileName.endswith(image_ext) or fileName.endswith(image_ext.upper()):
                moveFile(destinationDirImage, entry, fileName)
