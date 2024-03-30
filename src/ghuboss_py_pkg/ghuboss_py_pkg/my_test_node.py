import rclpy
from rclpy.node import Node


class MyTestNode(Node):
    def __init__(self):
        super().__init__('my_test_node')
        self.get_logger().info("my_test_node started!")

def main(args=None):
    rclpy.init(args=args)
    myNode = MyTestNode()

    rclpy.spin(myNode)

    myNode.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

