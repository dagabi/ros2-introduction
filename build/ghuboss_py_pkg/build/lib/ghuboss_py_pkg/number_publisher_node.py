import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
import random


class NumberPublisherNode(Node):
    def __init__(self):
        super().__init__('number_publisher_node')
        self._publisher = super().create_publisher(Int64, "number", 10)

        super().create_timer(1, self.publish_timer)

        self.get_logger().info("number_publisher_node started!")

    def publish_timer(self):
        msg = Int64()
        msg.data = random.randint(0,1000)
        self._publisher.publish(msg)
        self.get_logger().info(f"I just published number {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    myNode = NumberPublisherNode()

    rclpy.spin(myNode)

    myNode.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

