#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from std_msgs.msg import Float64
roll = pitch = yaw = 0.0

def get_rotation (msg):
    global roll, pitch, yaw
    orientation_q = msg.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
    pose_publisher = rospy.Publisher('/zebrat/theta', Float64, queue_size=1)
    pose_publisher.publish(yaw)

rospy.init_node('my_quaternion_to_euler')

sub = rospy.Subscriber ('/odom', Odometry, get_rotation)

r = rospy.Rate(1)
while not rospy.is_shutdown():    
    quat = quaternion_from_euler (roll, pitch,yaw)
    # print (quat)
    r.sleep()