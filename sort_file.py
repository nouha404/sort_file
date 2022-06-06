from os import mkdir
from pathlib import Path
import shutil
import os

"""
 mp3, wav, flac : Musique
 avi , mp4, gif : Videos
 bmp , png , jpg : images
 txt , pptx , csv , xls, odp , pages : Documents
 autres : Divers   
"""

SOURCE = Path(__file__).resolve()
ROOT = SOURCE.parent

#Dossier Musique
MUSIQUE = ROOT / 'Musique'
if not Path.exists(MUSIQUE):
    MUSIQUE.mkdir()
    
#Dossier Videos
VIDEOS = ROOT / 'Videos'
if not Path.exists(VIDEOS):
    VIDEOS.mkdir()
    
#Dossier Images
# [shutil.move(os.path.join(DATA_FOLDER,f.name),MUSIQUE) for f in DATA_FOLDER.glob('*.avi')]
IMAGES = ROOT / 'Images'
if not Path.exists(IMAGES):
    IMAGES.mkdir()

#Dossier Documents
DOCUMENT = ROOT / 'Documents'
if not Path.exists(DOCUMENT):
    DOCUMENT.mkdir()
    
#Dossier DIVERS
DIVERS = ROOT / 'Divers'
if not Path.exists(DIVERS):
    DIVERS.mkdir()
    
#DOSSIER AVEC LES DONNES
DATA_FILE = SOURCE.parent / 'data'
print(DATA_FILE)

for f in DATA_FILE.iterdir():
    
    if f.suffix ==  '.gif' or f.suffix ==  '.mp4' or f.suffix ==  '.avi':
        shutil.move(os.path.join(DATA_FILE,f.name),VIDEOS)
        
    elif f.suffix ==  '.mp3' or f.suffix ==  '.wav' or f.suffix ==  '.flac':
        shutil.move(os.path.join(DATA_FILE,f.name),MUSIQUE)
        
    elif f.suffix ==  '.bmp' or f.suffix ==  '.png' or f.suffix ==  '.jpg':
        shutil.move(os.path.join(DATA_FILE,f.name),IMAGES)
        
    elif f.suffix ==  '.txt' or f.suffix ==  '.pptx' or f.suffix ==  '.csv' or f.suffix ==  '.xls' or f.suffix ==  '.odp'  or f.suffix ==  '.pages':
        shutil.move(os.path.join(DATA_FILE,f.name),DOCUMENT)
    else:
        shutil.move(os.path.join(DATA_FILE,f.name),DIVERS)

