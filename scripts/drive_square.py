#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist, Vector3
import math

#constant vectors, corresponding to turning, standing still, and moving forward
turning_twist = Twist(linear = Vector3(), angular = Vector3(0, 0, math.pi / 4))
stopped = Twist(linear = Vector3(), angular = Vector3()) 
forward_twist = Twist(linear = Vector3(.5, 0, 0), angular = Vector3())

class DriveInSquare(object):
    def __init__(self):
        #node publishes to cmd_vel, just like exercises
        #starting vel is standing still
        rospy.init_node('Drive_in_circle')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.twist = stopped

    def go_forward(self):
        #tell turtle to move forward then halt
        #set rate of 2 hrtz 
        r = rospy.Rate(2)
        self.twist = forward_twist
        #tells turtle 10 times to move forward, twice every second
        #so moving forward for 5 seconds
        for i in range(10):
            self.pub.publish(self.twist)
            r.sleep()
        #after done moving forward, we halt then stop for a bit
        self.twist = stopped
        self.pub.publish(self.twist) 
        r.sleep()

    def turn(self):
        #tell turtle to turn 90 degrees then halt
        r = rospy.Rate(2)
        self.twist = turning_twist
        #angular velocity pi/4, do this for 2 seconds, so pi/2 radians
        for i in range(4):
            self.pub.publish(self.twist)
            r.sleep()
        #after done turning, stop moving
        self.twist = stopped
        self.pub.publish(self.twist)
        r.sleep()

    def run(self):
        #slight delay for ros to get prepared
        rospy.sleep(1)
        #loop 4 times, ie drive forward, turn, forward, turn, forward, turn, forward, turn
        #back to start
        for i in range(5) :
            self.go_forward()
            self.turn()


if __name__ == '__main__':
    #run the node
    node = DriveInSquare()
    node.run()