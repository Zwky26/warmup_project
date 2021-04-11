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
                #two conditions need to be met before we drive forward
                #right side is closest to wall, distance in sweet spot
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
            #turns until the closest wall is on right side of turtlebot
            self.twist.linear.x = 0
            if ind in range(135, 254):
                self.twist.angular.z = -0.2 
            else:
                self.twist.angular.z = 0.2
            self.pub.publish(self.twist)

        def drive_forward(self):
            #all conditions are a go, just drive forward
            self.twist.linear.x = 0.2
            self.twist.angular.z = 0
            self.pub.publish(self.twist)

        def drive_closer(self, distance):
            #wall is in right spot, but distance is not sweet spot
            #very slight adjustment to angle
            #note that this is VERY slow at start, bc it makes a big spiral
            #after close to wall serves as corrective turns 
            if distance > 0.8:
                self.twist.angular.z = -0.1
            else:
                self.twist.angular.z = 0.1
            self.twist.linear.x = 0.1
            self.pub.publish(self.twist)

        def run(self):
            #keeps it running
            rospy.spin()
                
if __name__ == '__main__':

        rospy.init_node('person_follower')
        follower = Follower()
        follower.run()