# HPCJobResultSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_id** | **int** |  | [optional] 
**result_type** | **str** |  | [optional] 

## Example

```python
from us3api.models.hpc_job_result_set import HPCJobResultSet

# TODO update the JSON string below
json = "{}"
# create an instance of HPCJobResultSet from a JSON string
hpc_job_result_set_instance = HPCJobResultSet.from_json(json)
# print the JSON string representation of the object
print(HPCJobResultSet.to_json())

# convert the object into a dict
hpc_job_result_set_dict = hpc_job_result_set_instance.to_dict()
# create an instance of HPCJobResultSet from a dict
hpc_job_result_set_from_dict = HPCJobResultSet.from_dict(hpc_job_result_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


