#!/bin/bash

deploy_msg='automatic deployment'

srv=${1:-remote.maxresing.de}
dir=${2:-/var/www/www.maxresing.de/html/}

dist="./site/*"


echo "Generating page and content..."
./makesite.py &> /dev/null
echo "Page generation finished."

echo "Commit '$deploy_msg'"
git add .
git commit -m "$deploy_msg"
git push

ssh ${srv} rm -rf ${dir}
echo "Removed existing files in ${dir}."

echo "Copying files to ${srv}:${dir}"
scp ${srv} -r $dist ${srv}:${dir} &> /dev/null
echo "Copied ${#dist[@]} files."

ssh ${srv} chown -R max:caddy ${dir}
echo "Changed ownership."

exit 0
