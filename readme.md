# Flask Streamer for Neural Networks

- [Flask Streamer for Neural Networks](#flask-streamer-for-neural-networks)
  - [Description](#description)
  - [Motivation](#motivation)
  - [Installation & Setup](#installation--setup)
  - [Known Issues](#known-issues)
  - [Disclaimer](#disclaimer)

## Description

This is a repo for a flask based webserver for an application capable of streaming as soon as possible the results of a neural network such as YOLO, Tensorflow or Pytorch based in a stream-like fashion for easier visualization.

## Motivation

This idea came as one of my projects for a subject in school, however I liked the results and wanted to share with the OpenSource community, just in case that someone else is having the same kind of issue and in need of some inspiration.

## Installation & Setup

If you only need the base server it is ok to just:

```bash
  $ git clone https://github.com/JOmarCuenca/flask-live-video-stream-yolo
  $ python3 -m venv env && source env/bin/activate
  $ pip install -r requirements.txt
  $ python3 app.py
```

After those commands you should have the base server up and running in no time.

However in order to get the demo working in case that you still need some inspiration.

```bash
  $ git clone https://github.com/JOmarCuenca/flask-live-video-stream-yolo
  $ python3 -m venv env && source env/bin/activate
  $ pip install -r requirements.txt
  $ git pull --recurse-submodules
  $ python3 app.py
```

This commands should also import a functioning version of a YOLO based NN for social distancing detection.

After that the only thing you need to do is configure your video streamer to use another service or NN of your choice.

## Known Issues
  - During the stream in the web-page there are instances in which the stream will fail to load, this is probably due to the difference in speed on which the server is trying to stream the next frame which hasn't been fully saved in disk by the NN. Or it could be sth else IDK.

## Disclaimer

This is an implementation of the original creator [Miguel Grinberg](https://github.com/miguelgrinberg/flask-video-streaming) who is the rightful owner of the original flask-video-streaming.

I just used the original implementation and build upon it to serve my demo's purposes.

I do not intend to take credit as the original LICENSE of Mr. Miguel Grinberg is located in the **originalFiles/** directory as instructed in his repo.
