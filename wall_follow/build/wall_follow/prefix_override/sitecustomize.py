import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/dohrmam/Downloads/497/ros-lab-2-dohrmam-main/wall_follow/install/wall_follow'
