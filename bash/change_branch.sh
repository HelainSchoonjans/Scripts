#!/bin/bash

# checkout a branch for each project folder in current folder
for D in */; do
	echo "------------ ${D}"
	cd "${D}"
	pwd
	git branch
	git checkout develop
	cd ..
done