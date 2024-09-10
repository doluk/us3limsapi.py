# HPCJobDataset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hpc_dataset_id** | **int** |  | [optional] 
**edited_data_id** | **int** |  | [optional] 
**raw_data_id** | **int** |  | [optional] 
**label** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**simpoints** | **int** |  | [optional] 
**band_volume** | **float** |  | [optional] 
**radial_grid** | [**RadialGrid**](RadialGrid.md) |  | [optional] [default to RadialGrid.ASTFEM]
**time_grid** | [**TimeGrid**](TimeGrid.md) |  | [optional] [default to TimeGrid.AST]
**noise** | **List[int]** |  | [optional] 

## Example

```python
from us3api.models.hpc_job_dataset import HPCJobDataset

# TODO update the JSON string below
json = "{}"
# create an instance of HPCJobDataset from a JSON string
hpc_job_dataset_instance = HPCJobDataset.from_json(json)
# print the JSON string representation of the object
print(HPCJobDataset.to_json())

# convert the object into a dict
hpc_job_dataset_dict = hpc_job_dataset_instance.to_dict()
# create an instance of HPCJobDataset from a dict
hpc_job_dataset_from_dict = HPCJobDataset.from_dict(hpc_job_dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


