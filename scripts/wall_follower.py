#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan
import math

class Follower:
        def __init__(self):
                # subscribe to the robot's RGB camera data stream
                self.person_sub = rospy.Subscriber('scan',
                        LaserScan, self.scan_callback)

                self.twist = Twist()
                self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

        def scan_callback(self, msg):
                #want to find the minimum of all elements in scan
                #this should tell us which way the wall is
                dist = min(msg.ranges)
                min_Ind = msg.ranges.index(dist)
                if min_Ind in range(245, 305):
                    if dist <= 0.8 and dist >= 0.4:
                        self.drive_forward()
                    else: 
                        self.drive_closer(dist) 
                else: 
                    self.orient(min_Ind)

        def orient(self, ind):
            self.twist.linear.x = 0
            if ind in range(135, 254):
                self.twist.angular.z = -0.2 
            else:
                self.twist.angular.z = 0.2
            self.pub.publish(self.twist)

        def drive_forward(self):
            self.twist.linear.x = 0.2
            self.twist.angular.z = 0
            self.pub.publish(self.twist)

        def drive_closer(self, distance):
            if distance > 0.8:
                self.twist.angular.z = -0.1
            else:
                self.twist.angular.z = 0.1
            self.twist.linear.x = 0.1
            self.pub.publish(self.twist)

        def run(self):
                rospy.spin()
                
if __name__ == '__main__':

        rospy.init_node('person_follower')
        follower = Follower()
        follower.run()