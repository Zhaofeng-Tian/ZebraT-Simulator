# ZebraT-Simulator
An ROS Simulator for an Autonomous Delivery Robot ZebraT

Paper link: [ZebraT Gazebo Simulator](https://arxiv.org/pdf/2205.07944.pdf)

# How to Use
1. Git clone the zebrat package to you ROS workspace.
2. Make this package under the workspace namespace.
`catkin_make ` to compile it and use `rospack profile` to update package list.
3. Test with `roslaunch zebrat zebrat_with_world.launch`
4. Expected result:
 <img src="./zsim.png" width = "50%" height = "50%" alt="Simulation" align=center />

5. Keyboard Control `rosrun zebrat keyboard_teleop.py`
6. Change Gazebo world in `/launch/zebrat_with_world.launch`
7. Change sensors in `/urdf/zebrat.urdf.xacro`
8. Test your own tasks.

# Paper
"Design and Implement an Enhanced Simulator for Autonomous Delivery Robot" MetroCAD 2022.

`@inproceedings{tian2022design,
  title={Design and implement an enhanced simulator for autonomous delivery robot},
  author={Tian, Zhaofeng and Shi, Weisong},
  booktitle={2022 Fifth International Conference on Connected and Autonomous Driving (MetroCAD)},
  pages={21--29},
  year={2022},
  organization={IEEE}
}`
