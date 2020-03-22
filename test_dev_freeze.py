import unittest

import logging
import logging.config

class FreezeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.INFO)

    def test_can_execute_fast_strategy(self):
        for i in range(1, 2000):
            logging.info("Am I gonna freeze now ? tentativ #{0}".format(i))

if __name__ == '__main__':
    unittest.main()
