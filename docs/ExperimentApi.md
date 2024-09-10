# us3api.ExperimentApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**experiments_experiment_id_get**](ExperimentApi.md#experiments_experiment_id_get) | **GET** /experiments/{experimentID} | 
[**experiments_experiment_id_hpcrequests_get**](ExperimentApi.md#experiments_experiment_id_hpcrequests_get) | **GET** /experiments/{experimentID}/hpcrequests | 
[**experiments_get**](ExperimentApi.md#experiments_get) | **GET** /experiments | 
[**experiments_search_get**](ExperimentApi.md#experiments_search_get) | **GET** /experiments/search | 


# **experiments_experiment_id_get**
> Experiment experiments_experiment_id_get(experiment_id)



Get an experiment by ID

### Example

* Basic Authentication (LIMSLogin):
* Api Key Authentication (USEmail):
* Api Key Authentication (USPassword):

```python
import us3api
from us3api.models.experiment import Experiment
from us3api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = us3api.Configuration(
    host = "http://localhost:3000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: LIMSLogin
configuration = us3api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: USEmail
configuration.api_key['USEmail'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['USEmail'] = 'Bearer'

# Configure API key authorization: USPassword
configuration.api_key['USPassword'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['USPassword'] = 'Bearer'

# Enter a context with an instance of the API client
async with us3api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = us3api.ExperimentApi(api_client)
    experiment_id = 56 # int | ID of experiment to return

    try:
        api_response = await api_instance.experiments_experiment_id_get(experiment_id)
        print("The response of ExperimentApi->experiments_experiment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentApi->experiments_experiment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_id** | **int**| ID of experiment to return | 

### Return type

[**Experiment**](Experiment.md)

### Authorization

[LIMSLogin](../README.md#LIMSLogin), [USEmail](../README.md#USEmail), [USPassword](../README.md#USPassword)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An experiment |  -  |
**404** | Experiment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiments_experiment_id_hpcrequests_get**
> List[HPCAnalysisRequest] experiments_experiment_id_hpcrequests_get(experiment_id)



Get a list of all HPC analysis requests for an experiment

### Example

* Basic Authentication (LIMSLogin):
* Api Key Authentication (USEmail):
* Api Key Authentication (USPassword):

```python
import us3api
from us3api.models.hpc_analysis_request import HPCAnalysisRequest
from us3api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = us3api.Configuration(
    host = "http://localhost:3000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: LIMSLogin
configuration = us3api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: USEmail
configuration.api_key['USEmail'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['USEmail'] = 'Bearer'

# Configure API key authorization: USPassword
configuration.api_key['USPassword'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['USPassword'] = 'Bearer'

# Enter a context with an instance of the API client
async with us3api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = us3api.ExperimentApi(api_client)
    experiment_id = 56 # int | ID of experiment to return

    try:
        api_response = await api_instance.experiments_experiment_id_hpcrequests_get(experiment_id)
        print("The response of ExperimentApi->experiments_experiment_id_hpcrequests_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentApi->experiments_experiment_id_hpcrequests_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_id** | **int**| ID of experiment to return | 

### Return type

[**List[HPCAnalysisRequest]**](HPCAnalysisRequest.md)

### Authorization

[LIMSLogin](../README.md#LIMSLogin), [USEmail](../README.md#USEmail), [USPassword](../README.md#USPassword)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of HPC analysis requests |  -  |
**404** | Experiment not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiments_get**
> List[Experiment] experiments_get()



Get a list of all experiments

### Example

* Basic Authentication (LIMSLogin):
* Api Key Authentication (USEmail):
* Api Key Authentication (USPassword):

```python
import us3api
from us3api.models.experiment import Experiment
from us3api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = us3api.Configuration(
    host = "http://localhost:3000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: LIMSLogin
configuration = us3api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: USEmail
configuration.api_key['USEmail'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['USEmail'] = 'Bearer'

# Configure API key authorization: USPassword
configuration.api_key['USPassword'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['USPassword'] = 'Bearer'

# Enter a context with an instance of the API client
async with us3api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = us3api.ExperimentApi(api_client)

    try:
        api_response = await api_instance.experiments_get()
        print("The response of ExperimentApi->experiments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentApi->experiments_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Experiment]**](Experiment.md)

### Authorization

[LIMSLogin](../README.md#LIMSLogin), [USEmail](../README.md#USEmail), [USPassword](../README.md#USPassword)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of experiments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiments_search_get**
> List[Experiment] experiments_search_get(project_id=project_id, run_id=run_id, label=label, project=project)



Search for experiments

### Example

* Basic Authentication (LIMSLogin):
* Api Key Authentication (USEmail):
* Api Key Authentication (USPassword):

```python
import us3api
from us3api.models.experiment import Experiment
from us3api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = us3api.Configuration(
    host = "http://localhost:3000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: LIMSLogin
configuration = us3api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: USEmail
configuration.api_key['USEmail'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['USEmail'] = 'Bearer'

# Configure API key authorization: USPassword
configuration.api_key['USPassword'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['USPassword'] = 'Bearer'

# Enter a context with an instance of the API client
async with us3api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = us3api.ExperimentApi(api_client)
    project_id = 56 # int | ID of project to search for (optional)
    run_id = 'run_id_example' # str | ID of run to search for (optional)
    label = 'label_example' # str | Label of experiment to search for (optional)
    project = 'project_example' # str | Description of project to search for (optional)

    try:
        api_response = await api_instance.experiments_search_get(project_id=project_id, run_id=run_id, label=label, project=project)
        print("The response of ExperimentApi->experiments_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentApi->experiments_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of project to search for | [optional] 
 **run_id** | **str**| ID of run to search for | [optional] 
 **label** | **str**| Label of experiment to search for | [optional] 
 **project** | **str**| Description of project to search for | [optional] 

### Return type

[**List[Experiment]**](Experiment.md)

### Authorization

[LIMSLogin](../README.md#LIMSLogin), [USEmail](../README.md#USEmail), [USPassword](../README.md#USPassword)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of experiments |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

