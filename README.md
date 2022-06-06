# sort_file
Ce script permet de trier un fichier selon son type ( suffix)

``` py
#Ce code permet de deplacer les fichier qui sont dans le chemin DATA_FILE vers le chemin VIDEOS qui a été crée en haut 
shutil.move(os.path.join(DATA_FILE,f.name),VIDEOS)

```

Je n'ai pas utiliser de comprehension de liste car je devais gerer tout les suffixes 
```py
[shutil.move(os.path.join(DATA_FOLDER,f.name),VIDEOS) for f in DATA_FOLDER.glob('*.avi')]
```

