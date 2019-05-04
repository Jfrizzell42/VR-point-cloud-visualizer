#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from math import radians
import threading
import os
import time


class checkForFile():
    def __init__(self):

        if os.path.exists("/home/jfrizzell42/PycharmProjects/TurtlebotMovement/file.txt") and os.path.getsize(
                "/home/jfrizzell42/PycharmProjects/TurtlebotMovement/file.txt") > 0:
            if os.path.getsize("/home/jfrizzell42/PycharmProjects/TurtlebotMovement/file.txt") == 1:
                Forward()
            elif os.path.getsize("/home/jfrizzell42/PycharmProjects/TurtlebotMovement/file.txt") == 2:
                Backward()
            elif os.path.getsize("/home/jfrizzell42/PycharmProjects/TurtlebotMovement/file.txt") == 3:
                Left()
            elif os.path.getsize("/home/jfrizzell42/PycharmProjects/TurtlebotMovement/file.txt") == 4:
                Right()
        else:
            print("theres no file here")


class Forward():
    def __init__(self):
        print("went forward")
        rospy.init_node('Forward', anonymous=False)

        self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)

        r = rospy.Rate(10);

        move_cmd = Twist()
        move_cmd.linear.x = 0.2
        move_cmd.angular.z = 0

        rospy.on_shutdown(self.shutdown)
        while not rospy.is_shutdown():
            for i in range(0, 10):
                self.cmd_vel.publish(move_cmd)
                r.sleep()
                count = count + 1
                if (count == 1):
                    shutdown()
                    sendOut()
                    
    def sendOut(self):
        f=f.open("output.txt", "w")
        f.write("Forward")
        f.close

    def shutdown(self):
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)


class Backward():
    def __init__(self):
        print("went backward")
        rospy.init_node('Backward', anonymous=False)

        self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)

        r = rospy.Rate(10);

        move_cmd = Twist()
        move_cmd.linear.x = -0.2
        move_cmd.angular.z = 0
        count = 0
        while not rospy.is_shutdown():
            for i in range(0,10):
                self.cmd_vel.publish(move_cmd)
                r.sleep()
                count = count + 1
                if (count ==1):
                    shutdown()
                    sendout()

    def sendOut(self):
        f=f.open("output.txt", "w")
        f.write("Backward")
        f.close


    def shutdown(self):
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)


class Left():
    def __init__(self):
        print("went left")

        rospy.init_node('Left', anonymous=False)

        self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)

        r = rospy.Rate(5);

        move_cmd = Twist()
        move_cmd.linear.y = 0.2
        move_cmd.angular.z = 0

        turn_cmd = Twist()
        turn_cmd.linear.x = 0
        turn_cmd.angular.z = radians(45);

        count = 0

        for x in range(0, 10):
            self.cmd_vel.publish(turn_cmd)
            r.sleep()
            count = count + 1
            if (count == 1):
                shutdown()
                sendout()
    def sendOut(self):
        f=f.open("output.txt", "w")
        f.write("left")
        f.close

    def shutdown(self):

        self.cmd_vel.publish(Twist())
        rospy.sleep(1)


class Right():
    def __init__(self):
        print("went right")
        rospy.init_node('Right', anonymous=False)

        self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)

        r = rospy.Rate(5);

        move_cmd = Twist()
        move_cmd.linear.y = 0.2
        move_cmd.angular.z = 0

        turn_cmd = Twist()
        turn_cmd.linear.x = 0
        turn_cmd.angular.z = radians(-45);

        count = 0

        for x in range(0, 10):
            self.cmd_vel.publish(turn_cmd)
            r.sleep()
            count = count + 1
            if (count == 1):
                shutdown()
                sendOut()
    def sendOut(self):
        f=f.open("output.txt", "w")
        f.write("Right")
        f.close
    def shutdown(self):

        self.cmd_vel.publish(Twist())
        rospy.sleep(1)


if __name__ == '__main__':
    checkForFile()
