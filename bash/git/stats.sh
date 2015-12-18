#!/bin/bash

# can summarise the contributions of various authors in a git repo
git shortlog -sne

# it can be useful to add a .mailmap file in the root of the folder content as example:
# Hélain Schoonjans <proper@email.com> <commit@email.com>
# see file:///C:/Program%20Files%20(x86)/Git/doc/git/html/git-shortlog.html