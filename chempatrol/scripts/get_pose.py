#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import Float32MultiArray
import yaml
#import urllib.request
import urllib

'''
def talker(goal_data):
    pub = rospy.Publisher('chatter', Float32MultiArray, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    #rate = rospy.Rate(10) # 10hz
    #while not rospy.is_shutdown():
    #hello_str = "auto"
    hello_str=Float32MultiArray()
    hello_str.data = goal_data;
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()
'''

if __name__ == '__main__':
    
    pub = rospy.Publisher('manual_pose', Float32MultiArray, queue_size=0)
    rospy.init_node('manual_control_get', anonymous=True)
    url = 'https://raw.githubusercontent.com/seeseeatre/justatestrun/master/target.txt'
    
    
    
    while not rospy.is_shutdown():
        rospy.sleep(1)
        '''try:
            # Download the file from `url`, save it in a temporary directory
            print("requesting file...")
            file_name, headers = urllib.urlretrieve(url)
            f = open(file_name, 'r')

        except:
            print("requesting file failed...")
            print("open local backup...")
            f = open('target.txt', 'r')
        
        lines = f.read().strip().split(',')
        
        print(lines, type(lines[1]))
        
        goal_data=list(map(float, lines))
        '''
        goal_data=[-1.24,-1.37,0.0,0.0,0.0,0.5,0.4,0.0]
        
        print(goal_data, type(goal_data[1]))
        
        try:
            
            hello_str=Float32MultiArray()
            hello_str.data = goal_data;
            rospy.loginfo(hello_str)
            pub.publish(hello_str)      
            #rate.sleep()
        except rospy.ROSInterruptException:
            pass
        
