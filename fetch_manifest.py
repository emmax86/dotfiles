#!/usr/local/bin/python
import shutil
import os

contents = []
with open("MANIFEST") as f:
    contents = f.readlines()
for line in contents:
    line = line.strip()
    if(line.endswith("/")):
        try:
            shutil.rmtree(line)
        except OSError:
            print "Could not remove %s. Assuming it is not present." % line
        shutil.copytree(os.path.expanduser("~") + "/" + line, line)
    else:
        try:
            os.remove(line)
        except OSError:
            print "Could not remove %s. Assuming it is not present." % line
        shutil.copy2(os.path.expanduser("~") + "/" + line, line)
