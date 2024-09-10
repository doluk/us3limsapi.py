# coding: utf-8

"""
    UltraScan 3 LIMS Database Instance API

    A more machine-accessible version of the UltraScan 3 LIMS functionality. The authentication is done using the user's US3 LIMS credentials and sending them with every request as header `Us-Email` and `Us-Password`. Alternatively Basic Auth can be used.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from us3api.models.hpc_job_parameters import HPCJobParameters

class TestHPCJobParameters(unittest.TestCase):
    """HPCJobParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HPCJobParameters:
        """Test HPCJobParameters
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HPCJobParameters`
        if include_optional:
            return HPCJobParameters(
                s_min = 1.337,
                s_max = 1.337,
                s_grid_points = 56,
                k_min = 1.337,
                k_max = 1.337,
                k_grid_points = 56,
                mc_iter = 56,
                max_iterations = 56,
                iterative = True,
                req_mgroupcount = 56,
                fit_ti_noise = True,
                fit_ri_noise = True,
                fit_mb = 'None',
                fit_mb_range = 1.337,
                fit_mb_points = 56,
                custom_grid_id = 56,
                simpoints = 56,
                band_volume = 1.337,
                radial_grid = 'ASTFEM',
                time_grid = 'AST'
            )
        else:
            return HPCJobParameters(
        )


    def testHPCJobParameters(self):
        """Test HPCJobParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
