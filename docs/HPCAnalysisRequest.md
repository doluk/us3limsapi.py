# HPCAnalysisRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hp_crequest_id** | **int** |  | 
**experiment_id** | **int** |  | [optional] 
**queue_status** | [**HPCAnalysisQueueStatus**](HPCAnalysisQueueStatus.md) |  | [optional] [default to HPCAnalysisQueueStatus.QUEUED]
**last_message** | **str** |  | [optional] 
**update_time** | **datetime** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**gfac_id** | **str** |  | [optional] 
**investigator_guid** | **str** |  | [optional] 
**submitter_guid** | **str** |  | [optional] 
**submit_time** | **datetime** |  | [optional] 
**cluster** | **str** |  | [optional] 
**method** | [**HPCAnalysisMethod**](HPCAnalysisMethod.md) |  | [optional] [default to HPCAnalysisMethod.ENUM_2_DSA]
**anal_type** | **str** |  | [optional] 
**datasets** | [**List[HPCJobDataset]**](HPCJobDataset.md) |  | [optional] 
**results** | [**List[HPCJobResultSet]**](HPCJobResultSet.md) |  | [optional] 

## Example

```python
from us3api.models.hpc_analysis_request import HPCAnalysisRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HPCAnalysisRequest from a JSON string
hpc_analysis_request_instance = HPCAnalysisRequest.from_json(json)
# print the JSON string representation of the object
print(HPCAnalysisRequest.to_json())

# convert the object into a dict
hpc_analysis_request_dict = hpc_analysis_request_instance.to_dict()
# create an instance of HPCAnalysisRequest from a dict
hpc_analysis_request_from_dict = HPCAnalysisRequest.from_dict(hpc_analysis_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


