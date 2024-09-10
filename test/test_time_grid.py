# coding: utf-8

"""
    UltraScan 3 LIMS Database Instance API

    A more machine-accessible version of the UltraScan 3 LIMS functionality. The authentication is done using the user's US3 LIMS credentials and sending them with every request as header `Us-Email` and `Us-Password`. Alternatively Basic Auth can be used.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from us3api.models.time_grid import TimeGrid

class TestTimeGrid(unittest.TestCase):
    """TimeGrid unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTimeGrid(self):
        """Test TimeGrid"""
        inst = TimeGrid()

if __name__ == '__main__':
    unittest.main()
