# us3api.HPCRequestApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hpcrequests_hpc_request_id_get**](HPCRequestApi.md#hpcrequests_hpc_request_id_get) | **GET** /hpcrequests/{hpcRequestID} | 
[**hpcrequests_post**](HPCRequestApi.md#hpcrequests_post) | **POST** /hpcrequests | 
[**hpcrequests_search_get**](HPCRequestApi.md#hpcrequests_search_get) | **GET** /hpcrequests/search | 


# **hpcrequests_hpc_request_id_get**
> HPCAnalysisRequest hpcrequests_hpc_request_id_get(hpc_request_id)



Get an HPC analysis request by ID

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
    api_instance = us3api.HPCRequestApi(api_client)
    hpc_request_id = 56 # int | ID of HPC analysis request to return

    try:
        api_response = await api_instance.hpcrequests_hpc_request_id_get(hpc_request_id)
        print("The response of HPCRequestApi->hpcrequests_hpc_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HPCRequestApi->hpcrequests_hpc_request_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hpc_request_id** | **int**| ID of HPC analysis request to return | 

### Return type

[**HPCAnalysisRequest**](HPCAnalysisRequest.md)

### Authorization

[LIMSLogin](../README.md#LIMSLogin), [USEmail](../README.md#USEmail), [USPassword](../README.md#USPassword)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An HPC analysis request |  -  |
**404** | HPC analysis request not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hpcrequests_post**
> HPCRequestSubmission hpcrequests_post(hpc_analysis_request_body)



Create a new HPC analysis request

### Example

* Basic Authentication (LIMSLogin):
* Api Key Authentication (USEmail):
* Api Key Authentication (USPassword):

```python
import us3api
from us3api.models.hpc_analysis_request_body import HPCAnalysisRequestBody
from us3api.models.hpc_request_submission import HPCRequestSubmission
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
    api_instance = us3api.HPCRequestApi(api_client)
    hpc_analysis_request_body = us3api.HPCAnalysisRequestBody() # HPCAnalysisRequestBody | 

    try:
        api_response = await api_instance.hpcrequests_post(hpc_analysis_request_body)
        print("The response of HPCRequestApi->hpcrequests_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HPCRequestApi->hpcrequests_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hpc_analysis_request_body** | [**HPCAnalysisRequestBody**](HPCAnalysisRequestBody.md)|  | 

### Return type

[**HPCRequestSubmission**](HPCRequestSubmission.md)

### Authorization

[LIMSLogin](../README.md#LIMSLogin), [USEmail](../README.md#USEmail), [USPassword](../README.md#USPassword)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HPC analysis request created |  -  |
**400** | Invalid request |  -  |
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
    api_instance = us3api.HPCRequestApi(api_client)
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
        print("The response of HPCRequestApi->hpcrequests_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HPCRequestApi->hpcrequests_search_get: %s\n" % e)
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

