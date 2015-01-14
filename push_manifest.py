#!/usr/local/bin/python
import shutil
import os

contents = []
with open("MANIFEST") as f:
    contents = f.readlines()
home_dir = os.path.expanduser("~") + "/"
for line in contents:
    line = line.strip()
    if(line.endswith("/")):
        try:
            shutil.rmtree(home_dir + line)
        except OSError:
            print "Could not remove %s. Assuming it is not present." % line
        shutil.copytree(line, home_dir + line)
    else:
        try:
            os.remove(home_dir + line)
        except OSError:
            print "Could not remove %s. Assuming it is not present." % line
        shutil.copy2(line, home_dir + line)
