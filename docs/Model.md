# Model


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **int** |  | 
**description** | **str** |  | 
**global_type** | [**GlobalType**](GlobalType.md) |  | [default to GlobalType.NORMAL]
**meniscus** | **float** | The meniscus used for the analysis producing this model | [optional] 
**mc_iteration** | **int** |  | [optional] 
**variance** | **float** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 
**ti_noise** | [**Noise**](Noise.md) |  | [optional] 
**ri_noise** | [**Noise**](Noise.md) |  | [optional] 
**edit** | [**EditedData**](EditedData.md) |  | [optional] 
**hp_crequest_id** | **int** |  | [optional] 

## Example

```python
from us3api.models.model import Model

# TODO update the JSON string below
json = "{}"
# create an instance of Model from a JSON string
model_instance = Model.from_json(json)
# print the JSON string representation of the object
print(Model.to_json())

# convert the object into a dict
model_dict = model_instance.to_dict()
# create an instance of Model from a dict
model_from_dict = Model.from_dict(model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


