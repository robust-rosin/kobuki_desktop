#!/usr/bin/env python

import sys
import unittest

import rospy

from rqt_robot_dashboard.widgets import MenuDashWidget

from kobuki_dashboard.led_widget import LedWidget
from kobuki_dashboard.motor_widget import MotorWidget

################################################################################
# Necessary Monkey Patching
################################################################################

class TestPublisher(object):
    def __init__(self, topic, msg_class, queue_size=None):
        if queue_size is None:
            raise ValueError("Queue size should not be None.")

rospy.Publisher = TestPublisher

def mock_init(self, topic, icons=None):
    pass

MenuDashWidget.__init__ = mock_init

def mock_setFixedSize(self, qsize):
    pass

MenuDashWidget.setFixedSize = mock_setFixedSize

def mock_add_action(self, name, action):
    pass

MenuDashWidget.add_action = mock_add_action


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
