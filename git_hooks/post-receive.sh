#!/bin/bash
repo_name=$(pwd |awk '{split($0,a,"/"); print a[5]}')
mkdir -p /home/git/docs/$repo_name

git_server_ip=$(hostname -I)

if ! [ -t 0 ]; then
  read -a ref
fi

IFS='/' read -ra REF <<< "${ref[2]}"
branch="${REF[2]}"

git --work-tree=/home/git/docs/$repo_name --git-dir=/home/git/version/$repo_name checkout -f


curl http://192.168.0.13:7000/tobuild -d "branch_name=$branch" -d "repo_name=$repo_name" -d "git_server=$git_server_ip" -X PUT


