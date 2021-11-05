import time
from base_camera import BaseCamera

__PROCESSED_FRAMES_PATH__   = "processedFrames"
__FRAMES_PER_SECOND__       = 30

PLACEHOLDER = open("./uploadedAssets/placeHolder.png","rb").read()

class StreamCamera(BaseCamera):

    index   = -1
    lastSuccess = None

    def __init__(self):
        super().__init__()
        StreamCamera.index = -1

    @staticmethod
    def get_current_frame(index : int):
        if(index == -1):
            StreamCamera.lastSuccess = None
            return PLACEHOLDER
        else:
            try:
                # print(f"Currently trying to print index {index}")
                f = open(f"{__PROCESSED_FRAMES_PATH__}/frame{index}.jpg", 'rb').read()
                if(index > StreamCamera.index):
                    StreamCamera.lastSuccess = time.time()
                StreamCamera.index = index
                return f
            except FileNotFoundError:
                # print(f"Error on index {ModifiedCamera.index}")
                notNone = (not StreamCamera.lastSuccess is None)
                # print(f"Last Success is not None {notNone}")
                lapsedTime = 0
                if(notNone):
                    lapsedTime = (time.time() - StreamCamera.lastSuccess)
                    # print(f"Lapsed Time {lapsedTime}")
                if(notNone and lapsedTime > 2):
                    StreamCamera.index = -1
                    StreamCamera.lastSuccess = None
                    return StreamCamera.get_current_frame(0)
                else:
                    return StreamCamera.get_current_frame(index - 1)


    @staticmethod
    def frames():
        while True:
            time.sleep(1/__FRAMES_PER_SECOND__)
            yield StreamCamera.get_current_frame(StreamCamera.index + 1)
