# Experiment

An experiment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment_id** | **int** |  | 
**last_updated** | **datetime** |  | 
**run_id** | **str** |  | 
**project_id** | **int** |  | 
**label** | **str** |  | 
**instrument_id** | **int** |  | [optional] 
**operator_id** | **int** |  | [optional] 
**rotor_id** | **int** |  | [optional] 
**rotor_calibration_id** | **int** |  | [optional] 
**experiment_guid** | **str** |  | [optional] 
**experiment_type** | [**ExperimentType**](ExperimentType.md) |  | [optional] [default to ExperimentType.VELOCITY]
**run_type** | [**RunType**](RunType.md) |  | [optional] 
**protocol_id** | **int** |  | [optional] 
**run_temp** | **float** |  | [optional] 
**date_begin** | **datetime** |  | [optional] 
**projects** | [**List[Project]**](Project.md) |  | [optional] 
**rawdata** | [**List[RawData]**](RawData.md) |  | [optional] 
**hp_crequests** | [**List[HPCAnalysisRequest]**](HPCAnalysisRequest.md) |  | [optional] 

## Example

```python
from us3api.models.experiment import Experiment

# TODO update the JSON string below
json = "{}"
# create an instance of Experiment from a JSON string
experiment_instance = Experiment.from_json(json)
# print the JSON string representation of the object
print(Experiment.to_json())

# convert the object into a dict
experiment_dict = experiment_instance.to_dict()
# create an instance of Experiment from a dict
experiment_from_dict = Experiment.from_dict(experiment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


