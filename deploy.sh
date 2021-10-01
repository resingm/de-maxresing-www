#!/bin/bash

deploy_msg='automatic deployment'

srv=${1:-remote.maxresing.de}
dir=${2:-/var/www/www.maxresing.de/html}

dist="./site/*"


echo "Generating new content..."
./makesite.py

echo "Commit '$deploy_msg'"
git add .
git commit -m "$deploy_msg"
git push

#ssh rm -rf /var/www/www.maxresing.de/html/
#echo "Removed existing files."

echo "Copying files to $srv..."
scp -r $dist $srv:$dir &> /dev/null
echo ""

echo "Copied ${#dist[@]} files sucessfully."

echo "Change owner to caddy"

exit 0
