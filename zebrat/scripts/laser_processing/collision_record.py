#!/usr/bin/env python3

from tokenize import cookie_re
import numpy as np
import rospy
import time

from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
from sensor_msgs.msg import Image
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from control_msgs.msg import JointControllerState
from ackermann_msgs.msg import AckermannDriveStamped
import time
from math import cos,sin,atan2,pi

linear = 0
steer = 0
ranges = []
class CollisionChecker():

    def __init__(self):
        rospy.logdebug("Start Initialization~~")
        rospy.init_node('collision_counter', anonymous=True)

        rospy.Subscriber("/scan", LaserScan, self.laser_scan_callback)
        # rospy.Subscriber("/zebrat/right_steering_hinge_position_controller/state",JointControllerState, steer_state_callback)
        # rospy.Subscriber("/zebrat/left_rear_wheel_velocity_controller/state",JointControllerState, speed_state_callback)

        self.ctr1 = 0
        self.ctr2 = 0
        self.ctr3 = 0

    def laser_scan_callback(self,data):
        ranges = []
        for i, item in enumerate(data.ranges):
            #if (i%mod==0):
            if item == float ('Inf') or np.isinf(item):
                ranges.append(6)
            elif np.isnan(item):
                ranges.append(0.1)
            else:
                ranges.append(round(item,2))

        self.checker1(ranges)
        self.checker2(ranges)
        self.checker3(ranges)
    
    def calculate_rect(self,x1,x2,w,n,dn):
        drange_index = []
        collision_ranges = []
        p1 = atan2(w,x2)
        p2 = atan2(x2,w)
        p3 = atan2(x1,w)
        p4 = atan2(w,x1)
        p5 = p4
        p6 = p3
        p7 = p2
        p8 = p1
        t1 = p1
        t2 = p1+p2
        t3 = p1+p2+p3
        t4 = p1+p2+p3+p4
        t5 = p1+p2+p3+p4+p5
        t6 = p1+p2+p3+p4+p5+p6
        t7 = p1+p2+p3+p4+p5+p6+p7

        # print(p1,p2,p3,p4)
        # print(t1,t2,t3,t4,t5,t6,t7)
        orig_interval = 2*pi/n
        d_interval = 2*pi/dn
        for i in range(dn):
            drange_index.append(round(d_interval*i/orig_interval))
        print(drange_index)
        for j in range(dn):
            angle = drange_index[j]*orig_interval
            if angle>=0 and angle < t1:
                collision_ranges.append(x2/cos(angle))
            elif angle >= t1 and angle < t2:
                collision_ranges.append(w/cos(angle-t1))
            elif angle >= t2 and angle < t3:
                collision_ranges.append(w/cos(angle-t2))
            elif angle >= t3 and angle < t4:
                collision_ranges.append(x1/cos(angle-t3))
            elif angle >= t4 and angle < t5:
                collision_ranges.append(x1/cos(angle-t4))
            elif angle >= t5 and angle <t6:
                collision_ranges.append(w/cos(angle-t5))
            elif angle >= t6 and angle < t7:
                collision_ranges.append(w/cos(angle-t6))
            else:
                collision_ranges.append(x2/cos(angle-t7))
            print(collision_ranges)

    def check(self,dranges,cranges):
        # check discretized_ranges and collision_ranges, return a bool
        for i in range(len(dranges)):
            if dranges[i] <= cranges[i]:
                return True
        return False


    def checker1(self, ranges):
        index = [0, 6, 12, 19, 22, 24, 28, 32, 38, 46, 58, 72, 90, 109, 118, 136, 180, 224, 242, 252, 270, 288, 302, 314, 322, 328, 332, 336, 338, 342, 348, 354]
        # cranges = [0.9, 0.905, 0.92, 0.906, 0.817, 0.73, 0.644, 0.562, 0.484, 0.414, 0.355, 0.315, 0.3, 0.302, 0.215, 0.138, 0.1, 0.138, 0.215, 0.315, 0.3, 0.315, 0.355, 0.414, 0.484, 0.562, 0.644, 0.73, 0.817, 0.944, 0.92, 0.905]
        # offset = [-0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.0, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02]
        # for i in range(len(cranges)):
        #     cranges[i] = cranges[i] - offset[i]
        # print(cranges)
        cranges = [0.92, 0.925, 0.9400000000000001, 0.926, 0.837, 0.75, 0.664, 0.5820000000000001, 0.504, 0.414, 0.45499999999999996, 0.41500000000000004, 0.4, 0.402, 0.315, 0.23800000000000002, 0.2, 0.23800000000000002, 0.315, 0.41500000000000004, 0.4, 0.41500000000000004, 0.45499999999999996, 0.434, 0.504, 0.5820000000000001, 0.664, 0.75, 0.837, 0.964, 0.9400000000000001, 0.925]
        dranges = []
        for i in range(len(index)):
            dranges.append(ranges[index[i]])
        is_collision = self.check(dranges,cranges)
        self.ctr1 = is_collision
        # print (" 1. Safty Region: ", str(is_collision))
        return is_collision
    def checker2(self, ranges):
        index = [0, 11, 22, 34, 45, 56, 68, 79, 90, 101, 112, 124, 135, 146, 158, 169, 180, 191, 202, 214, 225, 236, 247, 259, 270, 281, 292, 304, 315, 326, 337, 349]
        cranges = [0.9, 0.9168450254596928, 0.35002994750469274, 0.35884765166025384, 0.38238200794493454, 0.4259711095670057, 0.5108076563192698, 0.6558950244250084, 0.35, 0.35655084323432495, 0.10056094646777138, 0.10517883937835559, 0.11439589045541111, 0.13064526262847354, 0.16262537069321054, 0.22068179196479323, 0.1, 0.10187166949552143, 0.10785347426775835, 0.12062179485039054, 0.1414213562373095, 0.1788291649971402, 0.25593046652474527, 0.351307811142401, 0.35, 0.356550843234325, 0.37748715993715415, 0.422176281976367, 0.4949747468305832, 0.6259020774899906, 0.8957566328366083, 0.9145977783886985]
        dranges = []
        for i in range(len(index)):
            dranges.append(ranges[index[i]])
        is_collision = self.check(dranges,cranges)
        self.ctr2 = is_collision
        # print(" 2. FI Rect: ", str(is_collision))
        return is_collision
    def checker3(self, ranges):
        index = [0, 11, 22, 34, 45, 56, 68, 79, 90, 101, 112, 124, 135, 146, 158, 169, 180, 191, 202, 214, 225, 236, 247, 259, 270, 281, 292, 304, 315, 326, 337, 349]
        cranges = [0.365 for i in range(32)]
        dranges = []
        for i in range(len(index)):
            dranges.append(ranges[index[i]])
        is_collision = self.check(dranges,cranges)
        self.ctr3 = is_collision
        # print(" 3. FIFR: ", str(is_collision))
        return is_collision

if __name__ == '__main__':
    checker = CollisionChecker()
    i = 0
    counter = np.array([0, 0, 0])
    while i < 2000:
        print()
        if checker.ctr1 == 1 or checker.ctr2 == 1 or checker.ctr3 == 1:
            state = np.array([int(checker.ctr1),int(checker.ctr2),int(checker.ctr3)])
            counter += state
            print (counter)
        rospy.sleep(0.2)
        i += 1
    rospy.spin()
#     checker.calculate_rect(0.1,0.9,0.35,360,32)
# [502 404 342]
