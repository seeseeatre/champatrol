#!/usr/bin/env python

'''
Copyright (c) 2016, Xihan Bian
All rights reserved.
'''

import rospy
import yaml
from take_photo import TakePhoto
from go_to_specific_point_on_map import GoToPose
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray


#
# Once we recieve a manual control call
# 
def callback(data, navigator):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", str(data.data))
    print('manual_control A: ',manual_control)
    global manual_control
    print('manual_control B: ',manual_control)
    #global target_point
    #target_point[7] = 0.0
    if(data.data[7] == 1.0):
        rospy.loginfo('change to manual control')
        manual_control=True
        rospy.loginfo("Go to my pose in callback: ")
        p={'x':data.data[0],'y':data.data[1]}
        q={'r1': data.data[3], 'r2': data.data[4], 'r3': data.data[5], 'r4': data.data[6]}
        success = navigator.goto(p,q)


    elif(data.data[7] == 0.0):
        rospy.loginfo('change to auto patrol')
        manual_control=False
        print('manual_control D: ',manual_control)
    else:
        pass


if __name__ == '__main__':

    # Read route information from yaml file
    route = rospy.get_param("route")
    print(route)
    with open(route, 'r') as stream:
        dataMap = yaml.load(stream)
    #print('dataMap size: ', len(dataMap))
    state =0
    manual_control = False

    try:
        # Initialize
        rospy.init_node('follow_route', anonymous=False)
        navigator = GoToPose()
        camera = TakePhoto()
        rospy.Subscriber("manual_pose", Float32MultiArray, callback, navigator)
        
        
        while(not rospy.is_shutdown()):
            print('testpoint C, manual_control: ',manual_control)
            if(not manual_control):
                # go to next position, length of dataMap is the number of state
                state = (state+1)%len(dataMap)
                state_data=dataMap[state]
                
                name = state_data['filename']
                rospy.loginfo("Go to %s pose", name[:-4])
                success = navigator.goto(state_data['position'], state_data['quaternion'])
                if not success:
                    rospy.loginfo("Failed to reach %s pose", name[:-4])
                    continue
                rospy.loginfo("Reached %s pose", name[:-4])
                # after reaching position, take pic and save
                img_path = rospy.get_param("img_path")
                print(img_path+name)
                if camera.take_picture(img_path+name):
                    rospy.loginfo("Saved image " + name)
                else:
                    rospy.loginfo("No images received")
                #load the saved image and identify, could do this in the photo node
                # or just send this to another node and do the identification
                
                
            else:
                pass
                    
            rospy.sleep(1)
        
    except rospy.ROSInterruptException:
        rospy.loginfo("Ctrl-C caught. Quitting")
        exit(0)

