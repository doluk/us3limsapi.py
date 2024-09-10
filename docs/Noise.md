# Noise


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**noise_id** | **int** |  | 
**noise_type** | [**NoiseType**](NoiseType.md) |  | 
**description** | **str** |  | [optional] 
**time_entered** | **datetime** |  | 
**edited_data_id** | **int** |  | 
**model_id** | **int** |  | 

## Example

```python
from us3api.models.noise import Noise

# TODO update the JSON string below
json = "{}"
# create an instance of Noise from a JSON string
noise_instance = Noise.from_json(json)
# print the JSON string representation of the object
print(Noise.to_json())

# convert the object into a dict
noise_dict = noise_instance.to_dict()
# create an instance of Noise from a dict
noise_from_dict = Noise.from_dict(noise_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


