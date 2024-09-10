# HPCJobParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_min** | **float** |  | [optional] 
**s_max** | **float** |  | [optional] 
**s_grid_points** | **int** |  | [optional] 
**k_min** | **float** | This is called ff0_min in the US3 LIMS | [optional] 
**k_max** | **float** | This is called ff0_max in the US3 LIMS | [optional] 
**k_grid_points** | **int** | This is called ff0_points in the US3 LIMS | [optional] 
**mc_iter** | **int** | Number of Monte Carlo iterations | [optional] 
**max_iterations** | **int** | Maximum number of iterations | [optional] [default to 10]
**iterative** | **bool** | Whether to use iterative fitting | [optional] [default to False]
**req_mgroupcount** | **int** | Number of analysis mpi groups (each group has 1 master and n slaves) | [optional] [default to 1]
**fit_ti_noise** | **bool** | Fit the time-invariant noise | [optional] [default to False]
**fit_ri_noise** | **bool** | Fit the radial-invariant noise | [optional] [default to False]
**fit_mb** | [**MeniscusBottomFitType**](MeniscusBottomFitType.md) |  | [optional] 
**fit_mb_range** | **float** | Range of the meniscus and bottom fit | [optional] [default to 0.03]
**fit_mb_points** | **int** | Number of points to fit for the meniscus and bottom in the range | [optional] [default to 1]
**custom_grid_id** | **int** | ID of the custom grid, only used if radial_grid is Custom | [optional] [default to 0]
**simpoints** | **int** |  | [optional] [default to 100]
**band_volume** | **float** |  | [optional] [default to 0.0]
**radial_grid** | [**RadialGrid**](RadialGrid.md) |  | [optional] [default to RadialGrid.ASTFEM]
**time_grid** | [**TimeGrid**](TimeGrid.md) |  | [optional] [default to TimeGrid.AST]

## Example

```python
from us3api.models.hpc_job_parameters import HPCJobParameters

# TODO update the JSON string below
json = "{}"
# create an instance of HPCJobParameters from a JSON string
hpc_job_parameters_instance = HPCJobParameters.from_json(json)
# print the JSON string representation of the object
print(HPCJobParameters.to_json())

# convert the object into a dict
hpc_job_parameters_dict = hpc_job_parameters_instance.to_dict()
# create an instance of HPCJobParameters from a dict
hpc_job_parameters_from_dict = HPCJobParameters.from_dict(hpc_job_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


