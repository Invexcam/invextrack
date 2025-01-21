import os

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{subindent}{f}')

# Chemin de base de votre application
base_path = r"C:\Users\HP\Documents\App InvexTrack\InvexTrack v.0\invextrack\apps"

# Lister les fichiers et répertoires
list_files(base_path)