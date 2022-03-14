# only for usage at Dan Ortega's environments (adjust if interested)

import os
stream = os.popen('v4l2-ctl --list-devices')


line = ""
countLines = 0
camera = "NONE"

while True:
    line = stream.readline()
    countLines += 1

    if line.__contains__("Video Capture 4"):
        camera = stream.readline().strip()
        break

    if countLines == 15:
        break

print(camera)
