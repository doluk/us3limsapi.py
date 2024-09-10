# us3api.DataApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edits_edit_id_data_get**](DataApi.md#edits_edit_id_data_get) | **GET** /edits/{editID}/data | 
[**models_model_id_data_get**](DataApi.md#models_model_id_data_get) | **GET** /models/{modelID}/data | 
[**noises_noise_id_data_get**](DataApi.md#noises_noise_id_data_get) | **GET** /noises/{noiseID}/data | 
[**rawdata_raw_data_id_data_get**](DataApi.md#rawdata_raw_data_id_data_get) | **GET** /rawdata/{rawDataID}/data | 


# **edits_edit_id_data_get**
> Data edits_edit_id_data_get(edit_id)



Get the data of an edit by ID

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
    api_instance = us3api.DataApi(api_client)
    edit_id = 56 # int | ID of edit to return

    try:
        api_response = await api_instance.edits_edit_id_data_get(edit_id)
        print("The response of DataApi->edits_edit_id_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->edits_edit_id_data_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_id** | **int**| ID of edit to return | 

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
**200** | Edit Data |  -  |
**404** | Edit not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_model_id_data_get**
> Data models_model_id_data_get(model_id)



Get the data for a model

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
    api_instance = us3api.DataApi(api_client)
    model_id = 56 # int | ID of model to return data for

    try:
        api_response = await api_instance.models_model_id_data_get(model_id)
        print("The response of DataApi->models_model_id_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->models_model_id_data_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **int**| ID of model to return data for | 

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
**200** | The data for the model |  -  |
**404** | Model not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **noises_noise_id_data_get**
> Data noises_noise_id_data_get(noise_id)



Get the data for a noise

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
    api_instance = us3api.DataApi(api_client)
    noise_id = 56 # int | ID of noise to return data for

    try:
        api_response = await api_instance.noises_noise_id_data_get(noise_id)
        print("The response of DataApi->noises_noise_id_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->noises_noise_id_data_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **noise_id** | **int**| ID of noise to return data for | 

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
**200** | The data for the noise |  -  |
**404** | Noise not found |  -  |
**500** | Internal server error |  -  |

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
    api_instance = us3api.DataApi(api_client)
    raw_data_id = 56 # int | ID of raw data to return

    try:
        api_response = await api_instance.rawdata_raw_data_id_data_get(raw_data_id)
        print("The response of DataApi->rawdata_raw_data_id_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->rawdata_raw_data_id_data_get: %s\n" % e)
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

