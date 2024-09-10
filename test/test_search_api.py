# coding: utf-8

"""
    UltraScan 3 LIMS Database Instance API

    A more machine-accessible version of the UltraScan 3 LIMS functionality. The authentication is done using the user's US3 LIMS credentials and sending them with every request as header `Us-Email` and `Us-Password`. Alternatively Basic Auth can be used.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from us3api.api.search_api import SearchApi


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SearchApi()

    def tearDown(self) -> None:
        pass

    def test_experiments_search_get(self) -> None:
        """Test case for experiments_search_get

        """
        pass

    def test_hpcrequests_search_get(self) -> None:
        """Test case for hpcrequests_search_get

        """
        pass

    def test_persons_search_get(self) -> None:
        """Test case for persons_search_get

        """
        pass

    def test_rawdata_search_get(self) -> None:
        """Test case for rawdata_search_get

        """
        pass


if __name__ == '__main__':
    unittest.main()
