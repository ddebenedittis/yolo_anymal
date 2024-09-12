# YOLO ANYmal

Track the motion of the ANYmal robot in a video and display its path.

## Setup

Install [Docker Community Edition](https://docs.docker.com/engine/install/ubuntu/) (ex Docker Engine).

Create the python virtual environment and build the Docker image with
```shell
./setup.bash
```

## Usage

### Docker Container

Run the Docker container with
```shell
./run.bash
```

Run the training with
```shell
python3 anymal_tracking/train.py
```

Run the tests of the trained network with
```shell
python3 anymal_tracking/test_<i>.py
```

### Labelme

Activate the Python virtual environment with
```shell
source ./.venv/bin/activate
```

Run labelme with
```shell
labelme
```

Convert the labels produced by `labelme` to `yolo` format with
```shell
labelme2yolo --json_dir path/to/jsons --val_size 0.20 --test_size 0.20
```

### Results

<img src="https://raw.githubusercontent.com/ddebenedittis/media/main/yolo_anymal/yolo_anymal.png" width="640">

