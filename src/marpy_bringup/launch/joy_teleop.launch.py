"""Drive MARPY with a PS4 controller (USB, attached to WSL via usbipd).

Hold L1 (dead man's switch) and use the left stick.
"""

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    # Reads the controller (/dev/input/js0) and publishes /joy
    joy_node = Node(
        package="joy",
        executable="joy_node",
        name="joy_node",
        output="screen",
        parameters=[{"deadzone": 0.1}],
    )

    # Turns /joy into /cmd_vel
    teleop_node = Node(
        package="teleop_twist_joy",
        executable="teleop_node",
        name="teleop_twist_joy_node",
        output="screen",
        parameters=[{
            "enable_button": 4,
            "axis_linear.x": 1,
            "axis_angular.yaw": 0,
            "scale_angular.yaw": 2.0,
        }],
    )

    return LaunchDescription([
        joy_node,
        teleop_node,
    ])
