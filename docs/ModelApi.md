# us3api.ModelApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**models_model_id_data_get**](ModelApi.md#models_model_id_data_get) | **GET** /models/{modelID}/data | 
[**models_model_id_get**](ModelApi.md#models_model_id_get) | **GET** /models/{modelID} | 


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
    api_instance = us3api.ModelApi(api_client)
    model_id = 56 # int | ID of model to return data for

    try:
        api_response = await api_instance.models_model_id_data_get(model_id)
        print("The response of ModelApi->models_model_id_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelApi->models_model_id_data_get: %s\n" % e)
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

# **models_model_id_get**
> Model models_model_id_get(model_id)



Get a model by ID

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
    api_instance = us3api.ModelApi(api_client)
    model_id = 56 # int | ID of model to return

    try:
        api_response = await api_instance.models_model_id_get(model_id)
        print("The response of ModelApi->models_model_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelApi->models_model_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **int**| ID of model to return | 

### Return type

[**Model**](Model.md)

### Authorization

[LIMSLogin](../README.md#LIMSLogin), [USEmail](../README.md#USEmail), [USPassword](../README.md#USPassword)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A model |  -  |
**404** | Model not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

