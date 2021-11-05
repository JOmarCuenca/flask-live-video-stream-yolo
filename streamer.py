import cv2
from os import makedirs
from shutil import rmtree
from social_distancing.social_distancing_detector import FrameArgs, predictFrames

__processed_frames_path__ = "./processedFrames/"

def cleanAssets():
  rmtree(__processed_frames_path__, True)
  makedirs(__processed_frames_path__, exist_ok=True)

def breakVideoIntoFrames(path_to_video : str):
  vidcap = cv2.VideoCapture(path_to_video)
  success,image = vidcap.read()
  count = 0
  while success:
    modifiedImg = cv2.flip(image, 0)
    cv2.imwrite(__processed_frames_path__+"frame%d.jpg" % count, modifiedImg)
    success,image = vidcap.read()
    count += 1
  return count

def analyzeStream(path_to_video: str):
  print(" Begin analyzing ".upper().center(30,"="))
  cleanAssets()
  predictFrames(FrameArgs(path_to_video, __processed_frames_path__, "person"))

def cleanAndBreak(path_to_video : str):
  cleanAssets()
  return breakVideoIntoFrames(path_to_video)