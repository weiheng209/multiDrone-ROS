#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix

#custom msg
from px4ros.msg import gpsPosition

'''callback function'''
def callback1(data):
	rospy.loginfo("I heard cb1 %s",data.data) 
	global self_position
	self_position = data.data

def callback2(data):
	rospy.loginfo("I heard cb2 %s",data) 
	global neighbour_position
	neighbour_position = data

def control():
	pass

def commuciation_check():
	pass

def takeoff(height):
	pass

if __name__ == '__main__':
	self_position = NavSatFix()
	neighbour_position = gpsPosition()
	
	rospy.init_node('px4ros_leader_control', anonymous=True)
	pub = rospy.Publisher('serial_data_send', String, queue_size=20)
	rate = rospy.Rate(10) # 10hz

	#subscribe info from mavros
	rospy.Subscriber("/mavros/global_position/raw/fix", NavSatFix, callback1)
	#subscribe info from leader_control_decode
	rospy.Subscriber("neighbour_position", gpsPosition, callback2)

	while not rospy.is_shutdown():
		
		#pub.publish(globalPosition)
		#rospy.loginfo("%s",globalPosition)
		rate.sleep()

	#while !commuciation_check():
	#	print "Waiting for connection!"
	
	#print "Commucate ok! Read to fly!"
	#takeoff(3)

	#control()

	

	
	
