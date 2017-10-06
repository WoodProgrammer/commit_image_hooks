#!/bin/bash

echo "REPO adı"
read repo_adi



ssh git@gitserver "mkdir -p /home/git/docs/$repo_adi /home/git/docs/$repo_adi.git \ git init --bare /home/git/docs/$repo_adi.git/"
