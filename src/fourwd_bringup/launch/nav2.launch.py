from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from ament_index_python.packages import get_package_share_directory

import os


def generate_launch_description():

    nav2_params = os.path.join(
        get_package_share_directory('fourwd_bringup'),
        'config',
        'nav2',
        'nav2_params.yaml'
    )

    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('nav2_bringup'),
                'launch',
                'bringup_launch.py'
            )
        ),
        launch_arguments={
            'slam': 'True',
         'use_sim_time': 'True',
         'autostart': 'True',
         'params_file': nav2_params
        }.items()
    )

    return LaunchDescription([
        nav2
    ])