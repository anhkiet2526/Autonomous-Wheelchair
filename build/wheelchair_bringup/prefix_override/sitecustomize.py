import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/anhkiet/Autonomous-Wheelchair/install/wheelchair_bringup'
