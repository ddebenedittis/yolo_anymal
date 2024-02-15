#!/bin/bash

mkdir -p detect

# Create the Python virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
pip3 uninstall -y opencv-python
pip3 install opencv-python-headless

# Build the Docker image
MYUID="$(id -u $USER)"
MYGID="$(id -g $USER)"

docker build \
    --build-arg MYUID=${UID} \
    --build-arg MYGID=${GID} \
    --build-arg USER=${USER} \
    -t yolo_anymal .