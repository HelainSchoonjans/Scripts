#!/bin/bash

#-o print Only the matched parts of a matching line, with each part on a separate line.
#-H print the filename for each match.
#-n prefix each line of output with the 1 based line number.
#-R, -r recursively read all files under subdirectories.

grep -oHnr "some pattern"  *.txt

### a good alternative on windows:
#s = recursive, 
#p = skip non-printable characters, 
#i = case insensitive, 
#n = print line numbers
findstr /sinp /c:"string" *.groovy