# ZebraT-Simulator
An ROS Simulator for an Autonomous Delivery Robot ZebraT

# How to Use
1. Git it the zebrat package to you ROS workspace.
2. Make this package under the workspace namespace.
`catkin_make ` and use `rospack profile` to update package list.
3. Test with `roslaunch zebrat zebrat_with_world.launch`
4. Expected result:
![car](/zsim.png)[url]{:height="50%" width="50%"}
 <img src="./zsim.png" width = "300" height = "200" alt="图片名称" align=center />
5. Keyboard Control `rosrun zebrat keyboard_teleop.py`
6. Change Gazebo world in `/launch/zebrat_with_world.launch`
7. Change sensors in `/urdf/zebrat.urdf.xacro`

# Paper
"Design and Implement an Enhanced Simulator for Autonomous Delivery Robot"
will be submitted to MetroCAD 2022.
