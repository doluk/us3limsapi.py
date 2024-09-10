# us3api.RawDataApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rawdata_get**](RawDataApi.md#rawdata_get) | **GET** /rawdata | 
[**rawdata_raw_data_id_data_get**](RawDataApi.md#rawdata_raw_data_id_data_get) | **GET** /rawdata/{rawDataID}/data | 
[**rawdata_raw_data_id_get**](RawDataApi.md#rawdata_raw_data_id_get) | **GET** /rawdata/{rawDataID} | 
[**rawdata_raw_data_id_hpcrequests_get**](RawDataApi.md#rawdata_raw_data_id_hpcrequests_get) | **GET** /rawdata/{rawDataID}/hpcrequests | 
[**rawdata_raw_data_id_models_get**](RawDataApi.md#rawdata_raw_data_id_models_get) | **GET** /rawdata/{rawDataID}/models | 
[**rawdata_search_get**](RawDataApi.md#rawdata_search_get) | **GET** /rawdata/search | 


# **rawdata_get**
> List[RawData] rawdata_get()



Get a list of all raw data

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
    api_instance = us3api.RawDataApi(api_client)

    try:
        api_response = await api_instance.rawdata_get()
        print("The response of RawDataApi->rawdata_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RawDataApi->rawdata_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rawdata_raw_data_id_data_get**
> Data rawdata_raw_data_id_data_get(raw_data_id)



Get the data of a raw data by ID

### Example

* Basic Authentication (LIMSLogin):
* Api Key Authentication (USEmail):
* Api Key Authentication (USPassword):

```python
import us3api
from us3api.models.data import Data
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
    api_instance = us3api.RawDataApi(api_client)
    raw_data_id = 56 # int | ID of raw data to return

    try:
        api_response = await api_instance.rawdata_raw_data_id_data_get(raw_data_id)
        print("The response of RawDataApi->rawdata_raw_data_id_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RawDataApi->rawdata_raw_data_id_data_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_data_id** | **int**| ID of raw data to return | 

### Return type

[**Data**](Data.md)

### Authorization

[LIMSLogin](../README.md#LIMSLogin), [USEmail](../README.md#USEmail), [USPassword](../README.md#USPassword)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Raw data |  -  |
**404** | Raw data not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rawdata_raw_data_id_get**
> RawData rawdata_raw_data_id_get(raw_data_id)



Get raw data by ID

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
    api_instance = us3api.RawDataApi(api_client)
    raw_data_id = 56 # int | ID of raw data to return

    try:
        api_response = await api_instance.rawdata_raw_data_id_get(raw_data_id)
        print("The response of RawDataApi->rawdata_raw_data_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RawDataApi->rawdata_raw_data_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_data_id** | **int**| ID of raw data to return | 

### Return type

[**RawData**](RawData.md)

### Authorization

[LIMSLogin](../README.md#LIMSLogin), [USEmail](../README.md#USEmail), [USPassword](../README.md#USPassword)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Raw data |  -  |
**404** | Raw data not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rawdata_raw_data_id_hpcrequests_get**
> List[HPCAnalysisRequest] rawdata_raw_data_id_hpcrequests_get(raw_data_id)



Get a list of all HPC analysis requests for a raw data

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
    api_instance = us3api.RawDataApi(api_client)
    raw_data_id = 56 # int | ID of raw dataset to return

    try:
        api_response = await api_instance.rawdata_raw_data_id_hpcrequests_get(raw_data_id)
        print("The response of RawDataApi->rawdata_raw_data_id_hpcrequests_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RawDataApi->rawdata_raw_data_id_hpcrequests_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_data_id** | **int**| ID of raw dataset to return | 

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
**404** | RawData not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rawdata_raw_data_id_models_get**
> List[Model] rawdata_raw_data_id_models_get(raw_data_id)



Get a list of all models for a raw data set

### Example

* Basic Authentication (LIMSLogin):
* Api Key Authentication (USEmail):
* Api Key Authentication (USPassword):

```python
import us3api
from us3api.models.model import Model
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
    api_instance = us3api.RawDataApi(api_client)
    raw_data_id = 56 # int | ID of rawdata to return models for

    try:
        api_response = await api_instance.rawdata_raw_data_id_models_get(raw_data_id)
        print("The response of RawDataApi->rawdata_raw_data_id_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RawDataApi->rawdata_raw_data_id_models_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_data_id** | **int**| ID of rawdata to return models for | 

### Return type

[**List[Model]**](Model.md)

### Authorization

[LIMSLogin](../README.md#LIMSLogin), [USEmail](../README.md#USEmail), [USPassword](../README.md#USPassword)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of models |  -  |
**404** | RawData not found |  -  |
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
    api_instance = us3api.RawDataApi(api_client)
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
        print("The response of RawDataApi->rawdata_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RawDataApi->rawdata_search_get: %s\n" % e)
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

