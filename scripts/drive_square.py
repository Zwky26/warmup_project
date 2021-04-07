#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist, Vector3
import math

turning_twist = Twist(linear = Vector3(), angular = Vector3(0, 0, math.pi))
stopped = Twist(linear = Vector3(), angular = Vector3()) 
forward_twist = Twist(linear = Vector3(1, 0, 0), angular = Vector3())

class DriveInSquare(object):
    def __init__(self):
        rospy.init_node('Drive_in_circle')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.twist = stopped
        #default, blank twist to start

    def go_forward(self):
        self.twist = forward_twist
        self.pub.publish(self.twist)
        rospy.sleep(3)
        self.twist = stopped
        self.pub.publish(self.twist)

    def turn(self):
        self.twist = turning_twist
        self.pub.publish(self.twist)
        rospy.sleep(1)
        self.twist = stopped
        self.pub.publish(self.twist)


    def run(self):
        for i in range(0, 4) :
            self.go_forward()
            rospy.sleep(5)
            self.turn()
            rospy.sleep(5)


if __name__ == '__main__':
    node = DriveInSquare()
    node.run()