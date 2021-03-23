import os, sys, shutil, glob
from sys import argv



src_adr = argv

def cleaner(src_adr):
    os.chdir(src_adr)
    path_file = os.listdir(src_adr)
    for file in path_file:
        if file.endswith(expancion_main) and os.path.abspath(file) != dest_dr:
            #print(os.path.abspath(file))
            shutil.move(os.path.abspath(file), dest_dr)
            print('file moved --- %s' % file)





