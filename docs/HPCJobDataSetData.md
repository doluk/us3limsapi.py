# HPCJobDataSetData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edit_id** | **int** | ID of the data edit, -1 for latest edit | [optional] [default to -1]
**raw_data_id** | **int** | ID of the raw data, will use automatically the latest edit if edit_id is -1 or not provided | [optional] 
**ri_noise** | **int** | ID of the ri noise data, -1 for latest noise, 0 for no noise | [optional] [default to -1]
**ti_noise** | **int** | ID of the ti noise data, -1 for latest noise, 0 for no noise | [optional] [default to -1]
**simpoints** | **int** |  | [optional] [default to 200]
**band_volume** | **float** |  | [optional] [default to 0.0]
**radial_grid** | [**RadialGrid**](RadialGrid.md) |  | [optional] [default to RadialGrid.ASTFEM]
**time_grid** | [**TimeGrid**](TimeGrid.md) |  | [optional] [default to TimeGrid.AST]

## Example

```python
from us3api.models.hpc_job_data_set_data import HPCJobDataSetData

# TODO update the JSON string below
json = "{}"
# create an instance of HPCJobDataSetData from a JSON string
hpc_job_data_set_data_instance = HPCJobDataSetData.from_json(json)
# print the JSON string representation of the object
print(HPCJobDataSetData.to_json())

# convert the object into a dict
hpc_job_data_set_data_dict = hpc_job_data_set_data_instance.to_dict()
# create an instance of HPCJobDataSetData from a dict
hpc_job_data_set_data_from_dict = HPCJobDataSetData.from_dict(hpc_job_data_set_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


