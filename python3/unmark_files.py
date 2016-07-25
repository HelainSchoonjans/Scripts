"""

See mark_file_as_changed.py.

Removes the "//CHANGED" comments in all the files of the folder.

Created on Tue Jul 19 14:04:51 2016

@author: hschoonjans

Python 3
"""

import os
import sys

walk_dir = sys.argv[1]

print('walk_dir = ' + walk_dir)

READ_MODE = 'r'
WRITE_MODE = 'w'

for root, subdirs, files in os.walk(walk_dir):
    print('--\nroot = ' + root)

    for filename in files:
        file_path = os.path.join(root, filename)

        print('\t- file %s (full path: %s)' % (filename, file_path))

        f = open(file_path, READ_MODE)
        file_data = f.read()
        f.close()

        new_data = file_data.replace("//CHANGED", "")

        f = open(file_path, WRITE_MODE)
        f.write(new_data)
        f.close()
