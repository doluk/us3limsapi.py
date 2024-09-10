# coding: utf-8

"""
    UltraScan 3 LIMS Database Instance API

    A more machine-accessible version of the UltraScan 3 LIMS functionality. The authentication is done using the user's US3 LIMS credentials and sending them with every request as header `Us-Email` and `Us-Password`. Alternatively Basic Auth can be used.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from us3api.api.data_api import DataApi


class TestDataApi(unittest.TestCase):
    """DataApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DataApi()

    def tearDown(self) -> None:
        pass

    def test_edits_edit_id_data_get(self) -> None:
        """Test case for edits_edit_id_data_get

        """
        pass

    def test_models_model_id_data_get(self) -> None:
        """Test case for models_model_id_data_get

        """
        pass

    def test_noises_noise_id_data_get(self) -> None:
        """Test case for noises_noise_id_data_get

        """
        pass

    def test_rawdata_raw_data_id_data_get(self) -> None:
        """Test case for rawdata_raw_data_id_data_get

        """
        pass


if __name__ == '__main__':
    unittest.main()
