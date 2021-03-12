#!/bin/bash

deploy_msg='automatic deployment'

srv=${1:-remote.maxresing.de}
dir=${2:-/var/www/www.maxresing.de/html}

dist="./site/*"


echo "Generating new content..."
./makesite.py

echo Commit "$deploy_msg"
git add .
git commit -m "$deploy_msg"
git push

echo Copying files to $srv...
scp -r $dist $srv:$dir

echo Copied ${#dist[@]} files sucessfully.

exit 0
