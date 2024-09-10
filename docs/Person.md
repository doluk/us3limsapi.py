# Person


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person_id** | **int** |  | 
**person_guid** | **str** |  | 
**email** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**activated** | **bool** |  | 
**username** | **str** |  | [optional] 
**advanced_level** | **bool** |  | [optional] 
**user_level** | **int** |  | [optional] 
**cluster_authorizations** | **str** |  | [optional] 
**cluster_nodes** | [**List[ClusterNode]**](ClusterNode.md) |  | [optional] 

## Example

```python
from us3api.models.person import Person

# TODO update the JSON string below
json = "{}"
# create an instance of Person from a JSON string
person_instance = Person.from_json(json)
# print the JSON string representation of the object
print(Person.to_json())

# convert the object into a dict
person_dict = person_instance.to_dict()
# create an instance of Person from a dict
person_from_dict = Person.from_dict(person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


