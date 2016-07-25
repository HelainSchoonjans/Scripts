"""

This script appends comments to all files in the folder whose path is given as parameter, to ensure that
Intellij IDEA rebuilds them. This is useful to ensure that classes that implements a trait are recompiled when that trait is edited.

After compilation, please run the unmark files to remove the added comments.

Created on Tue Jul 19 14:04:51 2016

@author: hschoonjans

Python 3
"""

import os
import sys

walk_dir = sys.argv[1]

print('walk_dir = ' + walk_dir)

print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

APPEND = 'a'

for root, subdirs, files in os.walk(walk_dir):
    print('--\nroot = ' + root)

    for filename in files:
        file_path = os.path.join(root, filename)

        print('\t- file %s (full path: %s)' % (filename, file_path))

        with open(file_path, APPEND) as file:
            file.write("//CHANGED")
