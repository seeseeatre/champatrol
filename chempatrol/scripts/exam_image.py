#!/usr/bin/env python

import rospy
import cv2
import sys
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

import darknet

if __name__ == "__main__":

    rospy.init_node('obj_rec', anonymous=True)
    pub = rospy.Publisher('obj_rec_out', String, queue_size=10)
    
    net = darknet.load_net("/home/han/darknet/cfg/yolov3.cfg", "/home/han/darknet/yolov3.weights", 0)
    meta = darknet.load_meta("/home/han/darknet/cfg/coco.data")
    r = darknet.detect(net, meta, "/home/han/darknet/data/dog.jpg")
    
    print r
    
    pub.publish(str(r))
    
    rospy.spin()
