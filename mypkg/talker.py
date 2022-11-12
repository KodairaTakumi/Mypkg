import rclpy
from rclpy.node import Nodo
from std_msgs.msg import Int16

rclpy.init()
nodo = Node("talker")
pub = nodo.create_publisher(Int16,"countup",10)
n = 0

def cb():
    global n
    msg = Int16()
    msg.data = n
    pub.pblish(msg)
    n += 1

nodo.create_timer(0.5,cd)
rclpy.spin(node)
