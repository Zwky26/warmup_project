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
                #this should tell us which way the object is
                temp = min(msg.ranges)
                #stop at 1 unit away. If too close back up
                dist_err = temp - 1
                #index tells us rough angle, 0 is in front
                # index increases corresponds to clockwise around turtle
                min_Scanned_Ind = msg.ranges.index(temp)
                #angle_err = min_Scanned_Ind * 0.01
                if min_Scanned_Ind in list(range(10)) + list(range(349, 359)):
                    k_turn = 0
                elif min_Scanned_Ind in range(11, 179):
                    k_turn = 0.3
                else:
                    k_turn = -0.3
                k_forward = 0.15
                if math.isinf(temp): #no object exists, dont move
                    self.pub.publish(Twist())
                else: #object does exist, drive and turn towards
                    self.twist.linear.x = dist_err * k_forward
                    self.twist.angular.z = k_turn
                    self.pub.publish(self.twist)

        def run(self):
            #keep the scan running
                rospy.spin()
                
if __name__ == '__main__':

        rospy.init_node('person_follower')
        follower = Follower()
        follower.run()