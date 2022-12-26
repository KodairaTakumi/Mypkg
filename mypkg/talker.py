import rclpy
from rclpy.node import Node
from person_msgs.msg import Query

def cb(request, response):
    if request.name = "小平拓海":
        response.age = 20
    else:
        response.age = 44

    return response

rclpy.init()
node = Node("talker")
node.create_timer(0.5, cb)
rclpy.spin(node)
