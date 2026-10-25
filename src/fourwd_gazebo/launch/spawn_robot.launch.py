from launch import LaunchDescription

from launch.actions import ExecuteProcess

from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory
from launch.actions import TimerAction

import os


def generate_launch_description():

    world_file = os.path.join(
        get_package_share_directory('fourwd_gazebo'),
        'worlds',
        'room_world.sdf'
    )

    urdf_file = os.path.join(
        get_package_share_directory('fourwd_description'),
        'urdf',
        'fourwd_robot.urdf'
    )

    with open(urdf_file, 'r') as file:
        robot_description = file.read()

   

    gazebo = ExecuteProcess(
        cmd=[
            'gz',
            'sim',
            '-r',
            world_file
        ],
        output='screen'
    )

    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-string',
            robot_description,
            '-name',
            'fourwd_robot',
            '-x', '0.0',
            '-y', '0.0',
            '-z', '0.3'
        ],
        output='screen'
    )

    delayed_spawn = TimerAction(
        period=3.0,
        actions=[spawn_robot]
    )

    return LaunchDescription([
        
        gazebo,
        delayed_spawn
    ])
    
