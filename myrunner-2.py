# only for usage at Dan Ortega's environments (adjust if interested)

import os

stream = os.popen('v4l2-ctl --list-devices')

line = stream.readline()
if not line.__contains__("fake-cam"):
    print("MISSINGFAKE")
    exit()

countLines = 1
camera = "NONE"

while True:
    countLines += 1
    line = stream.readline()
    if line.__contains__("Trust Webcam"):
        camera = stream.readline().strip()
        break

    if countLines == 15:
        break

print(camera)
