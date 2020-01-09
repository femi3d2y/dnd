#!/bin/bash

gcloud compute instances create ${name}

gcloud compute instances add-tags ${name} --tags java-1

gcloud compute ssh ${name} << EOF

sudo apt update

sudo apt install -y openjdk-8-jdk

wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -

sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'

sudo apt update

sudo apt install -y jenkins

sudo chmod 777 /var/lib/jenkins/secrets/initialAdminPassword

touch .adminpass

sudo cat /var/lib/jenkins/secrets/initialAdminPassword > .adminpass

EOF


