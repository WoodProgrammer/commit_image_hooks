#!/bin/bash
repo_name=$(pwd |awk '{split($0,a,"/"); print a[4]}')
repo_docs_name=$(echo $repo_name |awk '{split($0,a,".");print a[1]}')

git --work-tree=/home/git/docs/$repo_docs_name --git-dir=/home/git/version/$repo_name checkout -f


docker build /home/git/docs/$repo_docs_name



