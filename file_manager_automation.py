#! /usr/bin/env python3 


# Module

import os
import watchdog
from time import sleep


#Directories

sourceDirectory = '/Users/mertdemirezen/Documents/Projects/FileManager'




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


with os.scandir(sourceDirectory) as entries :
    for entry in entries:
        print(entry)