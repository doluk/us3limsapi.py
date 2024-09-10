# RawData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_data_id** | **int** |  | 
**label** | **str** |  | 
**filename** | **str** |  | 
**comment** | **str** |  | [optional] 
**solution_id** | **int** |  | [optional] 
**experiment_id** | **int** |  | [optional] 
**run_id** | **str** |  | [optional] 
**last_updated** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**edits** | [**List[EditedData]**](EditedData.md) |  | [optional] 

## Example

```python
from us3api.models.raw_data import RawData

# TODO update the JSON string below
json = "{}"
# create an instance of RawData from a JSON string
raw_data_instance = RawData.from_json(json)
# print the JSON string representation of the object
print(RawData.to_json())

# convert the object into a dict
raw_data_dict = raw_data_instance.to_dict()
# create an instance of RawData from a dict
raw_data_from_dict = RawData.from_dict(raw_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


