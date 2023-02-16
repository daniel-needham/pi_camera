from picamera2 import Picamera2, Preview

picam2 = Picamera2()
picam2.start_preview(Preview.NULL)
try:
    #picam2.start_and_capture_file("test.jpg")
    picam2.start_and_record_video("test.mp4", duration=10)
    print("worked")
except:
    print("fail")
