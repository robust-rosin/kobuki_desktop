#!/usr/bin/env python

import sys
import unittest

import rospy

from kobuki_msgs.msg import Led, MotorPower

from kobuki_dashboard.led_widget import LedWidget
from kobuki_dashboard.motor_widget import MotorWidget

################################################################################
# Necessary Overrides
################################################################################

class TestPublisher(object):
    def __init__(self, topic, msg_class, queue_size=None):
        if queue_size is None:
            raise ValueError("Queue size should not be None.")

rospy.Publisher = TestPublisher

def mock_led_init(self, topic):
    self._pub = rospy.Publisher(topic, Led, queue_size=5)

LedWidget.__init__ = mock_led_init

def mock_motor_init(self, topic):
    self._pub = rospy.Publisher(topic, MotorPower, queue_size=5)

MotorWidget.__init__ = mock_motor_init


################################################################################
# Unit Test
################################################################################

## A sample python unit test
class TestQueueSize(unittest.TestCase):
    def test_led_widget_pub_queue_size(self):
        widget = LedWidget("/mobile_base/commands/led1")
        self.assertTrue(True)

    def test_motor_widget_pub_queue_size(self):
        widget = MotorWidget("/mobile_base/commands/motor_power")
        self.assertTrue(True)


if __name__ == "__main__":
    import rosunit
    rosunit.unitrun("kobuki_dashboard", "test_queue_size", TestQueueSize)
