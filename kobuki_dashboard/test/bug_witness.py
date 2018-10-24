#!/usr/bin/env python

import sys
import unittest

class BugWitness(unittest.TestCase):
    def test_import_qt(self):
        from kobuki_dashboard import battery_widget
        from kobuki_dashboard import dashboard
        self.assertTrue(True, 'assertion error')

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun('kobuki_dashboard', 'test_import_qt', BugWitness)
