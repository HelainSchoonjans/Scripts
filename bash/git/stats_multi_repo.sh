#!/bin/bash

# stats for each project folder in current folder
for D in */; do
	echo "------------ ${D}"
	cd "${D}"
	pwd
	git shortlog -sne
	cd ..
done