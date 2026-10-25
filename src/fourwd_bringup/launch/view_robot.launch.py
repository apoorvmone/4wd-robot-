from launch import LaunchDescription

from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

import os


def generate_launch_description():

    urdf_file = os.path.join(
        get_package_share_directory('fourwd_description'),
        'urdf',
        'fourwd_robot.urdf'
    )

    with open(urdf_file, 'r') as file:
        robot_description = file.read()

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[
            {
                'robot_description': robot_description,
                'use_sim_time': True
            }
        ]
    )

    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        output='screen',
        parameters=[
            {
                'use_sim_time': True
            }
        ]
       
    )
            

    return LaunchDescription([
        joint_state_publisher,
        robot_state_publisher
    ])