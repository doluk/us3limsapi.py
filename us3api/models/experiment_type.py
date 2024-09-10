# coding: utf-8

"""
    UltraScan 3 LIMS Database Instance API

    A more machine-accessible version of the UltraScan 3 LIMS functionality. The authentication is done using the user's US3 LIMS credentials and sending them with every request as header `Us-Email` and `Us-Password`. Alternatively Basic Auth can be used.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ExperimentType(str, Enum):
    """
    ExperimentType
    """

    """
    allowed enum values
    """
    VELOCITY = 'velocity'
    EQUILIBRIUM = 'equilibrium'
    DIFFUSION = 'diffusion'
    BUOYANCY = 'buoyancy'
    CALIBRATION = 'calibration'
    OTHER = 'other'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ExperimentType from a JSON string"""
        return cls(json.loads(json_str))


