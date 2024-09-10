# HPCRequestSubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **str** |  | 
**hp_crequest_ids** | **List[int]** | The IDs of the HPC requests that were submitted | 
**results** | **List[str]** | The results/errors of the submission(s) | 

## Example

```python
from us3api.models.hpc_request_submission import HPCRequestSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of HPCRequestSubmission from a JSON string
hpc_request_submission_instance = HPCRequestSubmission.from_json(json)
# print the JSON string representation of the object
print(HPCRequestSubmission.to_json())

# convert the object into a dict
hpc_request_submission_dict = hpc_request_submission_instance.to_dict()
# create an instance of HPCRequestSubmission from a dict
hpc_request_submission_from_dict = HPCRequestSubmission.from_dict(hpc_request_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


