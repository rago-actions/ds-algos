import os
import sys

if len(sys.argv) != 2:
    print("Please pass the absolute directiory path")
    sys.exit(1)

dir_path = sys.argv[1]

for dirpaths, dirs, files in os.walk(dir_path,topdown=False):
    for f in files:
        print("FILE: {}".format(os.path.join(dirpaths,f)))
        os.remove(os.path.join(dirpaths,f))

    for d in dirs:
        print("DIRS: {}".format(os.path.join(dirpaths,d)))
        os.rmdir(os.path.join(dirpaths,d))

os.rmdir(dir_path)
