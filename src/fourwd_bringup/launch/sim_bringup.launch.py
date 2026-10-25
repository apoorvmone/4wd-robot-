from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node


from launch.launch_description_sources import PythonLaunchDescriptionSource

from ament_index_python.packages import get_package_share_directory

import os


def generate_launch_description():
    lidar_tf = Node(
    package='tf2_ros',
    executable='static_transform_publisher',
    arguments=[
        '0', '0', '0',
        '0', '0', '0',
        'lidar_link',
        'fourwd_robot/base_footprint/gpu_lidar'
    ]
)
    bridge = Node(
    package='ros_gz_bridge',
    executable='parameter_bridge',
    output='screen',
    arguments=[
        '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
        '/scan@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan',
        '/odom@nav_msgs/msg/Odometry@gz.msgs.Odometry',
        '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
        '/model/fourwd_robot/tf@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V',
        '/camera/image_raw@sensor_msgs/msg/Image@gz.msgs.Image',
        '/camera/camera_info@sensor_msgs/msg/CameraInfo@gz.msgs.CameraInfo'
        
    ]
)

    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('fourwd_gazebo'),
                'launch',
                'spawn_robot.launch.py'
            )
        )
    )

    robot_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('fourwd_bringup'),
                'launch',
                'view_robot.launch.py'
            )
        )
    )
    slam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('slam_toolbox'),
                'launch',
                'online_async_launch.py'
        )
    )
)
    odom_tf = Node(
        package='fourwd_bringup',
        executable='odom_tf_broadcaster.py',
        output='screen',
        parameters=[
        {
            'use_sim_time': True
        }
    ]
    )

    lidar_tf = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=[
            '0', '0', '0',
            '0', '0', '0',
            'lidar_link',
            'fourwd_robot/base_footprint/gpu_lidar'
        ]
    )

    return LaunchDescription([
        gazebo_launch,
        robot_launch,
        bridge,
        odom_tf,
        lidar_tf,
        slam
    ])