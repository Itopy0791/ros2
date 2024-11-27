 1 import rclpy
 2 from rclpy.node import Node
 3 from person_msgs.msg import Person #変更
 4 
 5 rclpy.init()
 6 node = Node("talker")
 7 pub = node.create_publisher(Person, "person", 10) #変更
 8 n = 0
 9 
10 
11 def cb():
12     global n
13     msg = Person()         #送信するデータの型を変更
14     msg.name = "上田隆一"  #msgファイルに書いた「name」
15     msg.age = n            #msgファイルに書いた「age」
16     pub.publish(msg)
17     n += 1
18
20 def main():
21     node.create_timer(0.5, cb)
22     rclpy.spin(node)

