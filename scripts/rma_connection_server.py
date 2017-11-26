#!/usr/bin/env python
from std_srvs.srv import (Empty, EmptyResponse)
import rospy
import subprocess
import roslaunch
import signal

husky_child = None
class Jumpstart:
	husky_child = None

	def launch_husky(self, req):
		print "Launching husky simulator"
		self.husky_child = subprocess.Popen(["roslaunch", "husky_gazebo", "husky_empty_world.launch"])
		return EmptyResponse()

	def shutdown_husky(self, req):
		print "Shutting down husky simulator"
		self.husky_child.terminate()
		return EmptyResponse()

def rma_connection_server():
	rospy.init_node('rma_connection_server')
	starter = Jumpstart()
	launchHusky = rospy.Service('launch_husky', Empty, starter.launch_husky)
	shutdownHusky = rospy.Service('shutdown_husky', Empty, starter.shutdown_husky)
	print "Ready to launch husky"
	rospy.spin()

if __name__ == "__main__":
	rma_connection_server()