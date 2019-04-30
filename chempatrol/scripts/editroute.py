#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

route_file = open('route.txt', 'w')

pose_id =0

def callback(data):
    global pose_id
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.pose.position.x)
    pose = "- {filename: '"+str(pose_id)+".png', position: { x: "+str(data.pose.position.x)+", y: "+str(data.pose.position.y)+"}, quaternion: {r1: "+str(data.pose.orientation.x)+", r2: "+str(data.pose.orientation.y)+", r3: "+str(data.pose.orientation.z)+", r4: "+str(data.pose.orientation.w)+"}}"

    route_file.write(pose+"\n")

    pose_id = pose_id+1
    
def listener():
 
    rospy.init_node('listener', anonymous=True)
 
    rospy.Subscriber("/move_base_simple/goal", PoseStamped, callback)
 
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
 
if __name__ == '__main__':
    listener()

