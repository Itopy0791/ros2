 1 import rclpy
 2 from rclpy.node import Node
 3 from person_msgs.msg import Person
 4 
 5 
 6 rclpy.init()
 7 node = Node("listener")
 8 
 9 
10 def cb(msg):
11     global node
12     node.get_logger().info("Listen: %s" % msg)
13 
14 
15 def main():
16     pub = node.create_subscription(Person, "person", cb, 10)                 
17     rclpy.spin(node)
