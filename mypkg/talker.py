import rclpy
from rclpy.node import Node
import requests
from std_msgs.msg import String

class ISS_position(Node):
    def __init__(self):
        super().__init__("ISS_position")
        self.pub = self.create_publisher(String, "now_position", 10)
        self.create_timer(1.0, self.publish_ISS_position)

    def publish_ISS_position(self):
        data = self.get_iss_position()
        self.pub.publish(String(data=data))

    def get_iss_position(self):
        response = requests.get("http://api.open-notify.org/iss-now.json")
        if response.status_code == 200:
            iss_data = response.json()
            position = iss_data["iss_position"]
            return f"ISS Position: lat={position['latitude']}, lon={position['longitude']}"
        else:
            self.get_logger().warn(f"Failed to fetch ISS position, status code: {response.status_code}")
            return "Failed to fetch ISS position"
def main():
    rclpy.init()
    node = ISS_position()
    rclpy.spin(node)
