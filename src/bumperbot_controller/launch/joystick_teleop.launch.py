import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument


def generate_launch_description():

    debug_param = DeclareLaunchArgument('log_level', default_value='debug')

    joy_teleop = Node(
        package="joy_teleop",
        executable="joy_teleop",
        parameters=[os.path.join(get_package_share_directory("bumperbot_controller"), "config", "joy_teleop.yaml")],
        # arguments=['--ros-args', '--log-level', 'debug']

    )

    joy_node = Node(
        package="joy",
        executable="joy_node",
        name="joystick",
        parameters=[os.path.join(get_package_share_directory("bumperbot_controller"), "config", "joy_config.yaml")],
        # arguments=['--ros-args', '--log-level', 'debug']
    )

    return LaunchDescription(
        [
            debug_param,
            joy_teleop,
            joy_node
        ]
    )
