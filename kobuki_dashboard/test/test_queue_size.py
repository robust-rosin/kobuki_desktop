#!/usr/bin/env python

import sys
import unittest

import rospy

from kobuki_dashboard.led_widget import LedWidget
from kobuki_dashboard.motor_widget import MotorWidget

################################################################################
# ROS Python Overrides
################################################################################

class TestPublisher(object):
    def __init__(self, topic, msg_class, queue_size=None):
        if queue_size is None:
            raise ValueError("Queue size should not be None.")

rospy.Publisher = TestPublisher


################################################################################
# Unit Test
################################################################################

## A sample python unit test
class TestQueueSize(unittest.TestCase):
    @unittest.expectedFailure
    def test_led_widget_pub_queue_size(self):
        widget = LedWidget("/mobile_base/commands/led1")

    @unittest.expectedFailure
    def test_motor_widget_pub_queue_size(self):
        widget = MotorWidget("/mobile_base/commands/motor_power")


if __name__ == "__main__":
    import rosunit
    rosunit.unitrun("kobuki_dashboard", "test_queue_size", TestQueueSize)
