#!/bin/bash

sudo apt get update

sudo apt install python3

sudo apt install python3-pip

pip3 install virtualenv

mkdir project

cd project

python3 -m venv venv
