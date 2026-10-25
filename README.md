# 4WD Robot Simulation

A ROS 2 and Gazebo Sim workspace for a four-wheel-drive mobile robot with a LiDAR, camera, odometry, SLAM, and Nav2 support.

## What is included

- 4WD robot URDF with LiDAR and camera sensors
- Gazebo Sim room and tunnel worlds
- ROS–Gazebo bridge for simulation clock, LiDAR, odometry, velocity commands, and camera data
- SLAM Toolbox for building a map from the LiDAR scan
- Nav2 configuration for autonomous navigation

## Prerequisites

Use a ROS 2 installation that is compatible with Gazebo Sim and install the following ROS packages for your distribution:

```bash
sudo apt update
sudo apt install ros-${ROS_DISTRO}-ros-gz \
  ros-${ROS_DISTRO}-slam-toolbox \
  ros-${ROS_DISTRO}-nav2-bringup \
  ros-${ROS_DISTRO}-teleop-twist-keyboard
```

`colcon` and the usual ROS 2 development tools must also be installed. Source your ROS installation before every terminal session:

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
```

## Build the workspace

Clone the repository and build it from the workspace root:

```bash
git clone https://github.com/apoorvmone/4wd-robot-.git
cd 4wd-robot-
colcon build --symlink-install
source install/setup.bash
```

After changing a package, run `colcon build --symlink-install` again and re-source `install/setup.bash`.

## Run the room simulation

In the first terminal, start the complete simulation stack:

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
cd 4wd-robot-
source install/setup.bash
ros2 launch fourwd_bringup sim_bringup.launch.py
```

This opens the room world in Gazebo, spawns `fourwd_robot`, publishes the robot TF tree, bridges the sensor and control topics to ROS 2, and starts SLAM Toolbox.

## Drive the robot

Open a second terminal and send velocity commands with the keyboard:

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
cd 4wd-robot-
source install/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Use `i`, `j`, `k`, and `l` to move; press `q` or `z` to change speed. The command is published on `/cmd_vel` and bridged into Gazebo.

## View sensor data and the map

With the simulation running, these commands are useful in separate terminals:

```bash
# Confirm the bridged topics
ros2 topic list

# Inspect the LiDAR data
ros2 topic echo /scan --once

# Open RViz for the TF tree, laser scan, and SLAM map
rviz2
```

In RViz, set **Fixed Frame** to `map`, then add `Map` (topic `/map`), `LaserScan` (topic `/scan`), and `RobotModel` displays.

## Start Nav2

After starting the simulation, launch the project Nav2 configuration in another terminal:

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
cd 4wd-robot-
source install/setup.bash
ros2 launch fourwd_bringup nav2.launch.py
```

Nav2 uses simulation time and the parameters in `src/fourwd_bringup/config/nav2/nav2_params.yaml`. In RViz, use **Nav2 Goal** to place a goal pose after the map and transform tree are available.


