# coding: utf-8

"""
    UltraScan 3 LIMS Database Instance API

    A more machine-accessible version of the UltraScan 3 LIMS functionality. The authentication is done using the user's US3 LIMS credentials and sending them with every request as header `Us-Email` and `Us-Password`. Alternatively Basic Auth can be used.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from us3api.models.meniscus_bottom_fit_type import MeniscusBottomFitType
from us3api.models.radial_grid import RadialGrid
from us3api.models.time_grid import TimeGrid
from typing import Optional, Set
from typing_extensions import Self

class HPCJobParameters(BaseModel):
    """
    HPCJobParameters
    """ # noqa: E501
    s_min: Optional[Union[StrictFloat, StrictInt]] = None
    s_max: Optional[Union[StrictFloat, StrictInt]] = None
    s_grid_points: Optional[StrictInt] = None
    k_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="This is called ff0_min in the US3 LIMS")
    k_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="This is called ff0_max in the US3 LIMS")
    k_grid_points: Optional[StrictInt] = Field(default=None, description="This is called ff0_points in the US3 LIMS")
    mc_iter: Optional[StrictInt] = Field(default=None, description="Number of Monte Carlo iterations")
    max_iterations: Optional[StrictInt] = Field(default=10, description="Maximum number of iterations")
    iterative: Optional[bool] = Field(default=False, description="Whether to use iterative fitting")
    req_mgroupcount: Optional[StrictInt] = Field(default=1, description="Number of analysis mpi groups (each group has 1 master and n slaves)")
    fit_ti_noise: Optional[bool] = Field(default=False, description="Fit the time-invariant noise")
    fit_ri_noise: Optional[bool] = Field(default=False, description="Fit the radial-invariant noise")
    fit_mb: Optional[MeniscusBottomFitType] = None
    fit_mb_range: Optional[Union[StrictFloat, StrictInt]] = Field(default=0.03, description="Range of the meniscus and bottom fit")
    fit_mb_points: Optional[StrictInt] = Field(default=1, description="Number of points to fit for the meniscus and bottom in the range")
    custom_grid_id: Optional[StrictInt] = Field(default=0, description="ID of the custom grid, only used if radial_grid is Custom")
    simpoints: Optional[StrictInt] = 100
    band_volume: Optional[Union[StrictFloat, StrictInt]] = 0.0
    radial_grid: Optional[RadialGrid] = RadialGrid.ASTFEM
    time_grid: Optional[TimeGrid] = TimeGrid.AST
    __properties: ClassVar[List[str]] = ["s_min", "s_max", "s_grid_points", "k_min", "k_max", "k_grid_points", "mc_iter", "max_iterations", "iterative", "req_mgroupcount", "fit_ti_noise", "fit_ri_noise", "fit_mb", "fit_mb_range", "fit_mb_points", "custom_grid_id", "simpoints", "band_volume", "radial_grid", "time_grid"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of HPCJobParameters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HPCJobParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "s_min": obj.get("s_min"),
            "s_max": obj.get("s_max"),
            "s_grid_points": obj.get("s_grid_points"),
            "k_min": obj.get("k_min"),
            "k_max": obj.get("k_max"),
            "k_grid_points": obj.get("k_grid_points"),
            "mc_iter": obj.get("mc_iter"),
            "max_iterations": obj.get("max_iterations") if obj.get("max_iterations") is not None else 10,
            "iterative": obj.get("iterative") if obj.get("iterative") is not None else False,
            "req_mgroupcount": obj.get("req_mgroupcount") if obj.get("req_mgroupcount") is not None else 1,
            "fit_ti_noise": obj.get("fit_ti_noise") if obj.get("fit_ti_noise") is not None else False,
            "fit_ri_noise": obj.get("fit_ri_noise") if obj.get("fit_ri_noise") is not None else False,
            "fit_mb": obj.get("fit_mb"),
            "fit_mb_range": obj.get("fit_mb_range") if obj.get("fit_mb_range") is not None else 0.03,
            "fit_mb_points": obj.get("fit_mb_points") if obj.get("fit_mb_points") is not None else 1,
            "custom_grid_id": obj.get("custom_grid_id") if obj.get("custom_grid_id") is not None else 0,
            "simpoints": obj.get("simpoints") if obj.get("simpoints") is not None else 100,
            "band_volume": obj.get("band_volume") if obj.get("band_volume") is not None else 0.0,
            "radial_grid": obj.get("radial_grid") if obj.get("radial_grid") is not None else RadialGrid.ASTFEM,
            "time_grid": obj.get("time_grid") if obj.get("time_grid") is not None else TimeGrid.AST
        })
        return _obj


