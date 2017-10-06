#!/bin/bash

echo "REPO adı"
read repo_adi


ssh git@gitserver "mkdir -p /home/git/docs/$repo_adi \ mkdir -p /home/git/versions/$repo_adi.git "
ssh git@gitserver "git init --bare /home/git/versions/$repo_adi.git/"
