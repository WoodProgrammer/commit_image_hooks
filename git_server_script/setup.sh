#!/bin/bash

sudo -s 
apt-get update 
apt-get install git 
apt-get install git-core
git_server_ip=$(hostname -I)

echo "Git Kullanıcısı oluşturuluyor.."
adduser git 




echo "Git Kullanıcısı ssh key oluşturuluyor."
ssh-keygen 


echo "SSH Keyinizi giriniz : "
read key_of_me

touch /home/git/.ssh/authorized_keys
echo $key_of_me >> /home/git/.ssh/authorized_keys

echo "Key Eklendi .. "
echo "Git server :    git@$git_server_ip   "

echo "Git server a gitserver ismi ile ulaşabilmek için bu komutu local terminalinizde çalıştırın"
echo "Komut: \n"
echo  '$git_server_ip  gitserver ' >> /etc/hosts





