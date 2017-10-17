#!/bin/bash
repo_name=$(pwd |awk '{split($0,a,"/"); print a[4]}')
repo_docs_name=$(echo $repo_name |awk '{split($0,a,".");print a[1]}')


if ! [ -t 0 ]; then
  read -a ref
fi

IFS='/' read -ra REF <<< "${ref[2]}"
branch="${REF[2]}"

mkdir -p /home/git/test_branches/$repo_docs_name/$branch

git --work-tree=/home/git/test_branches/$repo_docs_name --git-dir=/home/git/version/$repo_name checkout -f


if [ $branch == 'master' ]; then

   docker build --tag "$repo_name-$branch"/home/git/test_branches/$repo_docs_name/$branch
   build_status=$($?)
   if [ build_status == 0 ]; then
        echo "Master Branch image tagged  $repo_name-$branch LATEST . "

        docker tag $repo_name-$branch:latest localhost:5000/$repo_name-$branch
        docker push localhost:5000/$repo_name-$branch

        echo "MASTER BRANCH DOCKER IMAGE PUSHED . "
   fi
else

   docker build --tag "$repo_name-$branch"/home/git/test_branches/$repo_docs_name/$branch
   build_status=$($?)
   if [ build_status == 0 ]; then
        echo "$branch  image tagged  $repo_name-$branch LATEST . "

        docker tag $repo_name-$branch:latest localhost:5000/$repo_name-$branch
        docker push localhost:5000/$repo_name-$branch

        echo "$branch BRANCH DOCKER IMAGE PUSHED . "
   fi


fi



