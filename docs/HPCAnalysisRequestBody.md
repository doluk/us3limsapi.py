# HPCAnalysisRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**separate_datasets** | **str** |  | [optional] [default to 'separate']
**datasets** | [**List[HPCJobDataSetData]**](HPCJobDataSetData.md) |  | [optional] 
**job_parameters** | [**HPCJobParameters**](HPCJobParameters.md) |  | [optional] 
**clusternode** | **str** |  | [optional] 
**investigator_id** | **int** | ID of the data owner in case you submit on behalf of someone else | [optional] 
**hpc_analysis_method** | [**HPCAnalysisMethod**](HPCAnalysisMethod.md) |  | [optional] [default to HPCAnalysisMethod.ENUM_2_DSA]

## Example

```python
from us3api.models.hpc_analysis_request_body import HPCAnalysisRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of HPCAnalysisRequestBody from a JSON string
hpc_analysis_request_body_instance = HPCAnalysisRequestBody.from_json(json)
# print the JSON string representation of the object
print(HPCAnalysisRequestBody.to_json())

# convert the object into a dict
hpc_analysis_request_body_dict = hpc_analysis_request_body_instance.to_dict()
# create an instance of HPCAnalysisRequestBody from a dict
hpc_analysis_request_body_from_dict = HPCAnalysisRequestBody.from_dict(hpc_analysis_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


