import math
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from sensor_msgs.msg import LaserScan

class LidarListener(Node):

    scan_ranges = None

    def __init__(self):
        super().__init__('dohrmam_lidar_listener')
        self.subscription = self.create_subscription(LaserScan, '/diff_drive/scan', self.listener_callback, 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

        self.publisher_ = self.create_publisher(Twist, '/diff_drive/cmd_vel', 10)


    def listener_callback(self, msg):
        self.scan_ranges = msg.ranges

    def timer_callback(self):
        if self.scan_ranges is not None:
            print(self.scan_ranges[0])
            print(self.scan_ranges[1])
            
            
            if self.scan_ranges[0] < 3.0:
                
                msg = Twist()
                msg.linear.x = 0.0
                msg.angular.z = -4.0

                self.publisher_.publish(msg)
            
            elif self.scan_ranges[1] > 1.8:
                # move toward wall

                msg = Twist()
                msg.linear.x = 1.0
                msg.angular.z = 0.5 * self.scan_ranges[1]

                self.publisher_.publish(msg)

            else:
                msg = Twist()
                msg.linear.x = 2.0
                msg.angular.z = -0.01

                self.publisher_.publish(msg)
            



def main(args=None):
    rclpy.init(args=args)

    listener = LidarListener()

    rclpy.spin(listener)

    listener.destroy_node()
    rsclpy.shutdown()

if __name__ == '__main__':
    main()