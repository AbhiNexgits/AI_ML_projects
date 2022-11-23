from demo import *

# modelUrl = "http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_320x320_coco17_tpu-8.tar.gz"
# modelUrl = "http://download.tensorflow.org/models/object_detection/tf2/20200711/efficientdet_d7_coco17_tpu-32.tar.gz"
modelUrl = "http://download.tensorflow.org/models/object_detection/tf2/20200711/faster_rcnn_resnet152_v1_640x640_coco17_tpu-8.tar.gz"
classFile = "coco.names"

# It used for Images
imagePath = "bicycle2.jpg"

# It used for video
# videoPath = "v2.mp4"

# It used for webcam
# videoPath = 0
threshold = 0.5

detector = Detector()
detector.readClasses(classFile)
detector.downloadModel(modelUrl)
detector.loadModel()

# below are the calling function for Image and video

detector.predictImage(imagePath, threshold)
# detector.predictVideo(videoPath, threshold)
