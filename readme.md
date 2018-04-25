Download the ros package found here: https://github.com/perrypwang/rma-ros-server.
Place the rma-ros-server into your local `~/catkin_ws/src` folder.
Build the package from the `catkin_ws` folder and run the package by executing the following commands:
```
cd ~/catkin_ws
source devel/setup.sh
catkin_make install
rosrun rma rma_connection_server.py
```
This will start the ROS node that will allow you to launch and shutdown the husky simulator through a ROS service.
