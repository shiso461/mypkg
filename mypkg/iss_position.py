# SPDX-FileCopyrightText: 2025 Soma Shirai <shiso461@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
import requests
from std_msgs.msg import String

class ISSPositionPublisher(Node):
    def __init__(self):
        super().__init__("iss_position_publisher")
        self.pub = self.create_publisher(String, "now_position", 10)
        self.create_timer(1.0, self.publish_iss_position)

    def publish_iss_position(self):
        msg = String()
        msg.data = self.get_iss_position()
        self.pub.publish(msg)

    def get_iss_position(self):
        response = requests.get("http://api.open-notify.org/iss-now.json")
        if response.status_code == 200:
            iss_data = response.json()
            position = iss_data["iss_position"]
            return f"ISS Position: lat={position['latitude']}, lon={position['longitude']}"
        else:
            return "Failed to fetch ISS position"

def main():
    rclpy.init()
    node = ISSPositionPublisher()
    rclpy.spin(node)
