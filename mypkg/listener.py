# SPDX-FileCopyrightText: 2025 Soma Shirai <shiso461@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ISSPositionListener(Node):
    def __init__(self):
        super().__init__("iss_position_listener")
        self.create_subscription(String,"now_position",self.listener_callback,10)

    def listener_callback(self,msg):
        self.get_logger().info(f"{msg.data}")

def main():
    rclpy.init()
    node = ISSPositionListener()
    rclpy.spin(node)
