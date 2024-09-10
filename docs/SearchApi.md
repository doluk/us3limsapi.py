# us3api.SearchApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**experiments_search_get**](SearchApi.md#experiments_search_get) | **GET** /experiments/search | 
[**hpcrequests_search_get**](SearchApi.md#hpcrequests_search_get) | **GET** /hpcrequests/search | 
[**persons_search_get**](SearchApi.md#persons_search_get) | **GET** /persons/search | 
[**rawdata_search_get**](SearchApi.md#rawdata_search_get) | **GET** /rawdata/search | 


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
    api_instance = us3api.SearchApi(api_client)
    project_id = 56 # int | ID of project to search for (optional)
    run_id = 'run_id_example' # str | ID of run to search for (optional)
    label = 'label_example' # str | Label of experiment to search for (optional)
    project = 'project_example' # str | Description of project to search for (optional)

    try:
        api_response = await api_instance.experiments_search_get(project_id=project_id, run_id=run_id, label=label, project=project)
        print("The response of SearchApi->experiments_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->experiments_search_get: %s\n" % e)
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

# **hpcrequests_search_get**
> List[HPCAnalysisRequest] hpcrequests_search_get(experiment_id=experiment_id, submit_time=submit_time, cluster=cluster, method=method, anal_type=anal_type, status=status, edited_data_id=edited_data_id, gfac_id=gfac_id)



Search for HPC analysis requests

### Example

* Basic Authentication (LIMSLogin):
* Api Key Authentication (USEmail):
* Api Key Authentication (USPassword):

```python
import us3api
from us3api.models.hpc_analysis_method import HPCAnalysisMethod
from us3api.models.hpc_analysis_queue_status import HPCAnalysisQueueStatus
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
    api_instance = us3api.SearchApi(api_client)
    experiment_id = 56 # int | ID of experiment to search for (optional)
    submit_time = '2013-10-20T19:20:30+01:00' # datetime | Time of submission to search for (optional)
    cluster = 'cluster_example' # str | Cluster to search for (optional)
    method = 2DSA # HPCAnalysisMethod | Method to search for (optional) (default to 2DSA)
    anal_type = 'anal_type_example' # str | Type of analysis to search for (optional)
    status = queued # HPCAnalysisQueueStatus | Status of request to search for (optional) (default to queued)
    edited_data_id = 56 # int | ID of edited data to search for (optional)
    gfac_id = 56 # int | ID of gfac to search for (optional)

    try:
        api_response = await api_instance.hpcrequests_search_get(experiment_id=experiment_id, submit_time=submit_time, cluster=cluster, method=method, anal_type=anal_type, status=status, edited_data_id=edited_data_id, gfac_id=gfac_id)
        print("The response of SearchApi->hpcrequests_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->hpcrequests_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_id** | **int**| ID of experiment to search for | [optional] 
 **submit_time** | **datetime**| Time of submission to search for | [optional] 
 **cluster** | **str**| Cluster to search for | [optional] 
 **method** | [**HPCAnalysisMethod**](.md)| Method to search for | [optional] [default to 2DSA]
 **anal_type** | **str**| Type of analysis to search for | [optional] 
 **status** | [**HPCAnalysisQueueStatus**](.md)| Status of request to search for | [optional] [default to queued]
 **edited_data_id** | **int**| ID of edited data to search for | [optional] 
 **gfac_id** | **int**| ID of gfac to search for | [optional] 

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **persons_search_get**
> List[Person] persons_search_get(email=email, first_name=first_name, last_name=last_name, username=username, person_id=person_id, person_guid=person_guid)



Search for persons

### Example

* Basic Authentication (LIMSLogin):
* Api Key Authentication (USEmail):
* Api Key Authentication (USPassword):

```python
import us3api
from us3api.models.person import Person
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
    api_instance = us3api.SearchApi(api_client)
    email = 'email_example' # str | Email of person to search for (optional)
    first_name = 'first_name_example' # str | First name of person to search for (optional)
    last_name = 'last_name_example' # str | Last name of person to search for (optional)
    username = 'username_example' # str | Username of person to search for (optional)
    person_id = 56 # int | personID of person to search for (optional)
    person_guid = 'person_guid_example' # str | personGUID of person to search for (optional)

    try:
        api_response = await api_instance.persons_search_get(email=email, first_name=first_name, last_name=last_name, username=username, person_id=person_id, person_guid=person_guid)
        print("The response of SearchApi->persons_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->persons_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email of person to search for | [optional] 
 **first_name** | **str**| First name of person to search for | [optional] 
 **last_name** | **str**| Last name of person to search for | [optional] 
 **username** | **str**| Username of person to search for | [optional] 
 **person_id** | **int**| personID of person to search for | [optional] 
 **person_guid** | **str**| personGUID of person to search for | [optional] 

### Return type

[**List[Person]**](Person.md)

### Authorization

[LIMSLogin](../README.md#LIMSLogin), [USEmail](../README.md#USEmail), [USPassword](../README.md#USPassword)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of persons |  -  |
**404** | No persons found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rawdata_search_get**
> List[RawData] rawdata_search_get(project_id=project_id, run_id=run_id, experiment_id=experiment_id, project=project, label=label, filename=filename, comment=comment, solution_id=solution_id)



Search for raw data

### Example

* Basic Authentication (LIMSLogin):
* Api Key Authentication (USEmail):
* Api Key Authentication (USPassword):

```python
import us3api
from us3api.models.raw_data import RawData
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
    api_instance = us3api.SearchApi(api_client)
    project_id = 56 # int | ID of project to search for (optional)
    run_id = 'run_id_example' # str | ID of run to search for (optional)
    experiment_id = 56 # int | ID of experiment to search for (optional)
    project = 'project_example' # str | Description of project to search for (optional)
    label = 'label_example' # str | Label of raw data to search for (optional)
    filename = 'filename_example' # str | Filename of raw data to search for (optional)
    comment = 'comment_example' # str | Comment of raw data to search for (optional)
    solution_id = 56 # int | ID of solution to search for (optional)

    try:
        api_response = await api_instance.rawdata_search_get(project_id=project_id, run_id=run_id, experiment_id=experiment_id, project=project, label=label, filename=filename, comment=comment, solution_id=solution_id)
        print("The response of SearchApi->rawdata_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->rawdata_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of project to search for | [optional] 
 **run_id** | **str**| ID of run to search for | [optional] 
 **experiment_id** | **int**| ID of experiment to search for | [optional] 
 **project** | **str**| Description of project to search for | [optional] 
 **label** | **str**| Label of raw data to search for | [optional] 
 **filename** | **str**| Filename of raw data to search for | [optional] 
 **comment** | **str**| Comment of raw data to search for | [optional] 
 **solution_id** | **int**| ID of solution to search for | [optional] 

### Return type

[**List[RawData]**](RawData.md)

### Authorization

[LIMSLogin](../README.md#LIMSLogin), [USEmail](../README.md#USEmail), [USPassword](../README.md#USPassword)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of raw data |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

