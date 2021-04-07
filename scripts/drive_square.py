#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist, Vector3
import math

turning_twist = Twist(linear = Vector3(), angular = Vector3(0, 0, math.pi / 2))
stopped = Twist(linear = Vector3(), angular = Vector3()) 
forward_twist = Twist(linear = Vector3(.5, 0, 0), angular = Vector3())

class DriveInSquare(object):
    def __init__(self):
        rospy.init_node('Drive_in_circle')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.twist = stopped

    def go_forward(self):
        r = rospy.Rate(2)
        self.twist = forward_twist
        for i in range(10):
            self.pub.publish(self.twist)
            r.sleep()
        self.twist = stopped
        self.pub.publish(self.twist) 

    def turn(self):
        r = rospy.Rate(2)
        self.twist = turning_twist
        for i in range(2):
            self.pub.publish(self.twist)
            r.sleep()
        self.twist = stopped
        self.pub.publish(self.twist)

    def run(self):
        rospy.sleep(1)
        for i in range(5) :
            self.go_forward()
            rospy.sleep(5)
            self.turn()
            rospy.sleep(5)


if __name__ == '__main__':
    node = DriveInSquare()
    node.run()