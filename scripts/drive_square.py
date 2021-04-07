#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist, Vector3
import math

class DriveInSquare(object):
    def __init__(self):
        rospy.init_node('Drive_in_circle')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.twist = Twist(linear = Vector3(), angular = Vector3()) 
        #default, blank twist to start

    def go_forward(self):
        self.twist.linear.x = 1
        self.twist.angular.z = 0
        self.pub.publish(self.twist)
        rospy.sleep(3)

    def turn(self):
        self.twist.linear.x = 0
        self.twist.angular.z = 2 * math.pi
        self.pub.publish(self.twist)
        rospy.sleep(.25)


    def run(self):
        for(i in range(0, 4)):
            self.go_forward(self)
            self.turn(self)

if __name__ == '__main__':
    node = StopAtWall()
    node.run()