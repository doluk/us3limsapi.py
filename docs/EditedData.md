# EditedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edited_data_id** | **int** |  | 
**raw_data_id** | **int** |  | [optional] 
**edit_guid** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 
**models** | [**List[Model]**](Model.md) | The models for this edit. For each model only the modelID, description and globalType are returned | [optional] 
**latest_noises** | [**List[Noise]**](Noise.md) | The latest noise data for this edit | [optional] 
**hp_crequest_id** | **int** | The latest HPC request for this edit | [optional] 

## Example

```python
from us3api.models.edited_data import EditedData

# TODO update the JSON string below
json = "{}"
# create an instance of EditedData from a JSON string
edited_data_instance = EditedData.from_json(json)
# print the JSON string representation of the object
print(EditedData.to_json())

# convert the object into a dict
edited_data_dict = edited_data_instance.to_dict()
# create an instance of EditedData from a dict
edited_data_from_dict = EditedData.from_dict(edited_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


