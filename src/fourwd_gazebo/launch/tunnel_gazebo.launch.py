from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node


def generate_launch_description():

    gazebo = ExecuteProcess(
        cmd=[
            'gz',
            'sim',
            '-r',
            '/home/apoorv/4wd1_ws/src/fourwd_gazebo/worlds/tunnel_world.sdf'
        ],
        output='screen'
    )

    return LaunchDescription([
        gazebo
    ])
