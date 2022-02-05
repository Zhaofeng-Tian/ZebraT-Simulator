#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def laser_callback(data):
  new_scan = data
  print len(data.ranges)
  # new_scan.ranges = [data.ranges[0],data.ranges[59],data.ranges[119],data.ranges[179],data.ranges[239],data.ranges[299]]
  # new_scan.ranges = [data.ranges[0],data.ranges[1],data.ranges[2],data.ranges[3],data.ranges4],data.ranges[5],data.ranges[6]]
  pub = rospy.Publisher('new_scan', LaserScan, queue_size =10)
  pub.publish(new_scan)	
  print new_scan.ranges

rospy.init_node('laser_processing')
laser_processing_sub = rospy.Subscriber('/scan', LaserScan, laser_callback)
rospy.spin()
